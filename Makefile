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
setup-core: setup
	git clone --branch $${RELEASE_BRANCH:-main} https://github.com/stolostron/multiclusterhub-operator
	git clone --branch $${BACKPLANE_BRANCH:-main} https://github.com/stolostron/backplane-operator
	mv multiclusterhub-operator/pkg/templates/crds ./acm-crds
	mv backplane-operator/pkg/templates/crds ./mce-crds
	rm -rf multiclusterhub-operator backplane-operator

.PHONY: remove-core-crds
remove-core-crds:
	rm -rf mce-crds acm-crds

.PHONY: setup
setup: deps
	@mkdir -p api-docs
	@printf "# This file ensures the .github directory is tracked by Git\n# Remove this file once you add workflow files to the directory" > api-docs/.gitkeep


.PHONY: gen-api-docs
gen-api-docs: setup
	python3 cmd/gen-api-docs.py $(SEARCH_DIR)

.PHONY: gen-api-docs-core
gen-api-docs-core: setup-core gen-api-docs remove-core-crds
	echo "API docs generated successfully"

# Test targets
.PHONY: test
#test: test-crd-import test-helm-template-removal test-integration
test: test-crd-import test-helm-template-removal test-clean
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

