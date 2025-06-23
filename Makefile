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

.PHONY: gen-api-docs
gen-api-docs: setup
	python3 cmd/gen-api-docs.py $${SEARCH_DIR}S

.PHONY: gen-api-docs-core
gen-api-docs-core: setup-core gen-api-docs remove-core-crds
	echo "API docs generated successfully"
