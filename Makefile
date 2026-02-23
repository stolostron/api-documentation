# Include common build rules (uncomment if you have a common.mk file)
# include common.mk

# Release branch configuration
# For different releases, set these environment variables:
# export RELEASE_BRANCH=release-2.10.0
# export BACKPLANE_BRANCH=release-2.10.0
# 
# Or run make with: RELEASE_BRANCH=release-2.10.0 BACKPLANE_BRANCH=release-2.10.0 make api-docs

SEARCH_DIR ?= .
FORCE_DOWNLOAD ?= false

# Default target - show available commands when no target is specified
.PHONY: help
help:
	@echo "Available make commands:"
	@echo ""
	@echo "Setup & Dependencies:"
	@echo "  ensure-gen-api-docs         - Download the API documentation generator script"
	@echo "  deps                        - Install Python, PyYAML, flake8, curl, and git if missing"
	@echo "  setup                       - Create api-docs directory and install dependencies"
	@echo "  setup-core                  - Clone repositories and set up core CRDs for ACM/MCE"
	@echo ""
	@echo "API Documentation Generation:"
	@echo "  generate                    - Generate API docs (prompts for release numbers if not set)"
	@echo "  gen-api-docs                - Generate API documentation from CRDs in current directory"
	@echo "  gen-api-docs-core           - Generate API documentation with core ACM/MCE CRDs"
	@echo ""
	@echo "Testing:"
	@echo "  test                        - Run all tests (CRD import, Helm template removal, AI output, and cleanup)"
	@echo "  lint                        - Run Python linting with flake8"
	@echo "  test-crd-import             - Test CRD import functionality"
	@echo "  test-helm-template-removal  - Test Helm template removal"
	@echo "  test-ai-output              - Test AI-consumable output (JSON schemas, example YAML, index)"
	@echo "  test-integration            - Run integration tests"
	@echo "  test-verbose                - Run all tests with verbose output"
	@echo "  test-clean                  - Clean up test artifacts (Python cache files and api-docs)"
	@echo ""
	@echo "Release Management:"
	@echo "  init-release                - Generate a new release workflow for GitHub Actions"
	@echo ""
	@echo "Development:"
	@echo "  dev-test                    - Complete development test cycle (clean + test)"
	@echo "  validate                    - Run tests and generate API docs for validation"
	@echo ""
	@echo "Cleanup:"
	@echo "  remove-git-repos            - Remove cloned git repositories"
	@echo "  remove-core-crds            - Remove MCE and ACM CRD directories"
	@echo "  clean                       - Complete cleanup (remove CRDs and git repos)"
	@echo ""
	@echo "Configuration Variables:"
	@echo "  SEARCH_DIR                  - Directory to search for CRDs (default: current directory)"
	@echo "  FORCE_DOWNLOAD              - Force re-download of gen-api-docs.py script (default: false)"
	@echo "  RELEASE_BRANCH              - Branch for multiclusterhub-operator (default: main)"
	@echo "  BACKPLANE_BRANCH            - Branch for backplane-operator and ocm (default: main)"
	@echo ""
	@echo "Example usage with custom branches:"
	@echo "  RELEASE_BRANCH=release-2.14.0 BACKPLANE_BRANCH=release-2.10.0 make gen-api-docs-core"
# Set help as the default target
.DEFAULT_GOAL := help

.PHONY: deps
deps: ensure-gen-api-docs
	@which python3 > /dev/null || (echo "Python3 not found. Attempting to install..." && (command -v apt-get >/dev/null 2>&1 && sudo apt-get update && sudo apt-get install -y python3) || (command -v yum >/dev/null 2>&1 && sudo yum install -y python3) || (command -v brew >/dev/null 2>&1 && brew install python3) || (echo "Automatic install failed. Please install Python3 manually." && exit 1))
	@python3 -c "import yaml" 2>/dev/null || (echo "PyYAML not found. Installing..." && python3 -m pip install --user pyyaml)
	@python3 -c "import flake8" 2>/dev/null || (echo "Flake8 not found. Installing..." && python3 -m pip install --user flake8)
	@which curl > /dev/null || (echo "Curl not found. Attempting to install..." && (command -v apt-get >/dev/null 2>&1 && sudo apt-get update && sudo apt-get install -y curl) || (command -v yum >/dev/null 2>&1 && sudo yum install -y curl) || (command -v brew >/dev/null 2>&1 && brew install curl) || (echo "Automatic install failed. Please install Curl manually." && exit 1))
	@which git > /dev/null || (echo "Git not found. Attempting to install..." && (command -v apt-get >/dev/null 2>&1 && sudo apt-get update && sudo apt-get install -y git) || (command -v yum >/dev/null 2>&1 && sudo yum install -y git) || (command -v brew >/dev/null 2>&1 && brew install git) || (echo "Automatic install failed. Please install Git manually." && exit 1))


.PHONY: ensure-gen-api-docs
ensure-gen-api-docs:
	@if [ ! -f cmd/gen-api-docs.py ] || [ "$${FORCE_DOWNLOAD}" = "true" ]; then \
		echo "cmd/gen-api-docs.py not found or FORCE_DOWNLOAD is true. Downloading..."; \
		mkdir -p cmd; \
		curl -sSL -o cmd/gen-api-docs.py https://raw.githubusercontent.com/stolostron/api-documentation/main/cmd/gen-api-docs.py; \
	fi

.PHONY: setup-core
setup-core: setup clean
	git clone --branch $${RELEASE_BRANCH:-main} https://github.com/stolostron/multiclusterhub-operator
	git clone --branch $${BACKPLANE_BRANCH:-main} https://github.com/stolostron/backplane-operator
	git clone --branch $${BACKPLANE_BRANCH:-main} https://github.com/stolostron/ocm.git
	mv multiclusterhub-operator/pkg/templates/crds ./acm-crds
	@if [ -d multiclusterhub-operator/pkg/templates/hosted-crds ]; then \
		mv multiclusterhub-operator/pkg/templates/hosted-crds ./acm-crds; \
	fi
	mv backplane-operator/pkg/templates/crds ./mce-crds
# Used cp to account for some CRD's already existing in the mce-crds directory
	cp -rn ocm/manifests/* ./mce-crds/
	@make remove-git-repos

.PHONY: remove-git-repos
remove-git-repos:
	rm -rf multiclusterhub-operator backplane-operator ocm

.PHONY: remove-core-crds
remove-core-crds:
	rm -rf mce-crds acm-crds

.PHONY: clean
clean: remove-core-crds remove-git-repos
	@echo "Cleaned up all files"

.PHONY: setup
setup: deps
	@mkdir -p api-docs
	@printf "# This file ensures the .github directory is tracked by Git\n# Remove this file once you add workflow files to the directory" > api-docs/.gitkeep


.PHONY: generate
generate:
	@if [ -z "$${RELEASE_BRANCH}" ]; then \
		read -p "Enter release number (e.g. 2.14.0): release-" release_num; \
		export RELEASE_BRANCH="release-$$release_num"; \
	fi; \
	if [ -z "$${BACKPLANE_BRANCH}" ]; then \
		read -p "Enter backplane release number (e.g. 2.10.0): backplane-" backplane_num; \
		export BACKPLANE_BRANCH="release-$$backplane_num"; \
	fi; \
	echo "Using RELEASE_BRANCH=$$RELEASE_BRANCH BACKPLANE_BRANCH=$$BACKPLANE_BRANCH"; \
	$(MAKE) RELEASE_BRANCH=$$RELEASE_BRANCH BACKPLANE_BRANCH=$$BACKPLANE_BRANCH gen-api-docs-core

.PHONY: gen-api-docs
gen-api-docs: setup
	python3 cmd/gen-api-docs.py $(SEARCH_DIR)

.PHONY: gen-api-docs-core
gen-api-docs-core: setup-core gen-api-docs
	@make remove-core-crds
	echo "API docs generated successfully"

# Release management targets
.PHONY: init-release
init-release:
	@read -p "Enter release version (e.g. 2.16): release-" release_ver; \
	read -p "Enter backplane version (e.g. 2.11): backplane-" backplane_ver; \
	RELEASE_BRANCH="release-$$release_ver"; \
	BACKPLANE_BRANCH="backplane-$$backplane_ver"; \
	WORKFLOW_FILE=".github/workflows/generate-api-docs-$${RELEASE_BRANCH}.yml"; \
	echo ""; \
	echo "  Release branch:  $$RELEASE_BRANCH"; \
	echo "  Backplane branch: $$BACKPLANE_BRANCH"; \
	echo "  Workflow file:    $$WORKFLOW_FILE"; \
	echo ""; \
	read -p "Proceed? [y/N] " confirm; \
	if [ "$$confirm" != "y" ] && [ "$$confirm" != "Y" ]; then \
		echo "Aborted."; \
		exit 1; \
	fi; \
	echo ""; \
	mkdir -p .github/workflows; \
	printf '%s\n' \
		"# .github/workflows/generate-api-docs-$${RELEASE_BRANCH}.yml" \
		"name: $${RELEASE_BRANCH}, Generate and Commit API Docs" \
		"" \
		"on:" \
		"  schedule:" \
		"    - cron: '0 0 * * *'" \
		"  workflow_dispatch:" \
		"" \
		"permissions:" \
		"  contents: write" \
		"  pull-requests: write" \
		"" \
		"jobs:" \
		"  generate-docs:" \
		"    runs-on: ubuntu-latest" \
		"" \
		"    env:" \
		"      RELEASE_BRANCH: '$$RELEASE_BRANCH'" \
		"      BACKPLANE_BRANCH: '$$BACKPLANE_BRANCH'" \
		"      FORCE_DOWNLOAD: 'true'" \
		"" \
		"    steps:" \
		"      - name: Checkout Repository" \
		"        uses: actions/checkout@v4" \
		"        with:" \
		'          ref: $${{ env.RELEASE_BRANCH }}' \
		"" \
		"      - name: Set up Python" \
		"        uses: actions/setup-python@v4" \
		"        with:" \
		"          python-version: '3.11'" \
		"" \
		"      - name: Generate API Documentation" \
		'        run: RELEASE_BRANCH=$${{ env.RELEASE_BRANCH }} BACKPLANE_BRANCH=$${{ env.BACKPLANE_BRANCH }} FORCE_DOWNLOAD=$${{ env.FORCE_DOWNLOAD }} make gen-api-docs-core' \
		"" \
		"      - name: Commit Documentation Changes" \
		"        uses: stefanzweifel/git-auto-commit-action@v5" \
		"        with:" \
		'          commit_message: "docs(api): Auto-generate API documentation for $${{ env.RELEASE_BRANCH }}"' \
		'          commit_user_name: "GitHub Actions Bot"' \
		'          commit_user_email: "github-actions[bot]@users.noreply.github.com"' \
		'          commit_author: "GitHub Actions Bot <github-actions[bot]@users.noreply.github.com>"' \
		"          file_pattern: api-docs/**" \
		'          branch: $${{ env.RELEASE_BRANCH }}' \
		> "$$WORKFLOW_FILE"; \
	echo "Created $$WORKFLOW_FILE"; \
	echo ""; \
	echo "Commit to main with:"; \
	echo "  git commit -m \"chore: add API docs generation workflow for $$RELEASE_BRANCH\""; \
	echo ""; \
	echo "Create the release branch with:"; \
	echo "  git branch $$RELEASE_BRANCH main && git push origin $$RELEASE_BRANCH"

# Test targets
.PHONY: test
#test: test-crd-import test-helm-template-removal test-integration
test: test-crd-import test-helm-template-removal test-ai-output test-clean
	@echo "✅ All tests passed!"

.PHONY: lint
lint: deps
	@echo "Running Python lint tests..."
	@python3 -m flake8 cmd/ tests/ --max-line-length=120 --ignore=E501,W503 --exclude=__pycache__

.PHONY: test-crd-import
test-crd-import: deps
	@echo "Running CRD import tests..."
	@python3 tests/run_tests.py --pattern test_crd_import.py

.PHONY: test-helm-template-removal
test-helm-template-removal: deps
	@echo "Running Helm template removal tests..."
	@python3 tests/run_tests.py --pattern test_helm_template_removal.py

.PHONY: test-ai-output
test-ai-output: deps
	@echo "Running AI output tests..."
	@python3 tests/run_tests.py --pattern test_ai_output.py

.PHONY: test-integration
test-integration: deps
	@echo "Running integration tests..."
	@python3 tests/run_tests.py --pattern test_integration.py

.PHONY: test-verbose
test-verbose: deps
	@echo "Running all tests with verbose output..."
	@python3 tests/run_tests.py --verbose

.PHONY: test-clean
test-clean:
	@echo "Cleaning up test artifacts..."
	@find . -name "*.pyc" -delete
	@find . -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null || true
	@rm -rf api-docs

# Development targets
.PHONY: dev-test
dev-test: test-clean test
	@echo "Development test cycle completed"

.PHONY: validate
validate: test gen-api-docs
	@echo "✅ Validation completed - all tests passed and API docs generated successfully"

