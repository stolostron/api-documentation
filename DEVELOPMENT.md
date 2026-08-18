# Development
## How to generate api-documentation for an indvidual repository
Check out the repository, then run the following commnads:
```
curl -o Makefile.api https://raw.githubusercontent.com/stolostron/api-documentation/main/Makefile && \
grep -q 'include Makefile.api' Makefile || sed -i '1i # See https://github.com/stolostron/api-documentation/blob/main/DEVELOPMENT.md for Makefile.api usage instructions\ninclude Makefile.api' Makefile
```

Now run
```
SEARCH_DIR=<path_to_crds_or_type.go> make gen-api-docs
```
Commit and push the changes.

### First-time GitHub Workflow Setup

For the first time setup, you need to download the GitHub workflow action and set up the automation:

1. **Create the workflows directory (if it doesn't exist):**
   ```sh
   mkdir -p .github/workflows
   ```

2. **Download the workflow file:**
   ```sh
   curl -o .github/workflows/generate-api-docs-release-2.14.yml https://raw.githubusercontent.com/stolostron/api-documentation/refs/heads/main/workflows/generate-api-docs-release-2.14.yml
   ```
3. **Rename and edit the workflow file:**
   ```sh
   mv .github/workflows/generate-api-docs-release-2.14.yml .github/workflows/generate-api-docs-release-{version}.yml
   ```

4. **Edit the workflow file:**
   - Open `.github/workflows/generate-api-docs-release-{version}.yml` in your editor
   - Update the environment variables to match your release:
     ```yaml
     env:
       RELEASE_BRANCH: 'release-{version}'
       PATH: '<path_to_crds_or_type.go>'
     ```

3. **Commit the workflow to your default branch:**
   ```sh
   git add .github/workflows/generate-api-docs-release-{version}.yml
   git commit -m "chore: add API docs workflow for release-{version}}"
   git push origin main # This is done because the workflows are only run from the default branch
   ```

Once committed to your default branch, the API documentation will start to be generated daily automatically.

## How to generate api-documentation for the core product

To add a new release, follow these steps:

1. **Run the release initializer on `main`:**
   ```sh
   make init-release
   ```
   Enter the release version (e.g. `2.17`) and backplane version (e.g. `2.12`). This will generate `.github/workflows/generate-api-docs-release-2.17.yml`.

2. **Commit and push the workflow to `main`:**
   ```sh
   git add .github/workflows/generate-api-docs-release-2.17.yml
   git commit -m "chore: add API docs generation workflow for release-2.17"
   git push upstream main
   ```

3. **Create and push the release branch:**
   ```sh
   git branch release-2.17 main
   git push upstream release-2.17
   ```

Once the workflow is committed to the default (`main`) branch, the API documentation will be generated daily automatically.
