deps:
.PHONY: deps
	@which python3 > /dev/null || (echo "Python3 not found. Attempting to install..." && (command -v apt-get >/dev/null 2>&1 && sudo apt-get update && sudo apt-get install -y python3) || (command -v yum >/dev/null 2>&1 && sudo yum install -y python3) || (command -v brew >/dev/null 2>&1 && brew install python3) || (echo "Automatic install failed. Please install Python3 manually." && exit 1))
	@python3 -c "import yaml" 2>/dev/null || (echo "PyYAML not found. Installing..." && python3 -m pip install --user pyyaml)
	@which curl > /dev/null || (echo "Curl not found. Attempting to install..." && (command -v apt-get >/dev/null 2>&1 && sudo apt-get update && sudo apt-get install -y curl) || (command -v yum >/dev/null 2>&1 && sudo yum install -y curl) || (command -v brew >/dev/null 2>&1 && brew install curl) || (echo "Automatic install failed. Please install Curl manually." && exit 1))
	@which git > /dev/null || (echo "Git not found. Attempting to install..." && (command -v apt-get >/dev/null 2>&1 && sudo apt-get update && sudo apt-get install -y git) || (command -v yum >/dev/null 2>&1 && sudo yum install -y git) || (command -v brew >/dev/null 2>&1 && brew install git) || (echo "Automatic install failed. Please install Git manually." && exit 1))

.PHONY: api-docs
api-docs: setup
	git clone git@github.com:stolostron/multiclusterhub-operator.git
	git clone git@github.com:stolostron/backplane-operator.git
	mv multiclusterhub-operator/pkg/templates/crds ./acm-crds
	mv backplane-operator/pkg/templates/crds ./mce-crds
	rm -rf multiclusterhub-operator backplane-operator
	python3 cmd/gen-api-docs.py
	rm -rf mce-crds acm-crds

setup: deps
.PHONY: setup
	@mkdir -p api-docs

