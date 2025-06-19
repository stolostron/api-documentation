# Development
## How to generate api-documentation for an indvidual repository
Check out the repository, then run the following commnads:
```
curl -o Makefile.api https://raw.githubusercontent.com/stolostron/api-documentation/main/Makefile && \
grep -q 'include Makefile.api' Makefile || sed -i '1i # See https://github.com/stolostron/api-documentation/blob/main/DEVELOPMENT.md for Makefile.api usage instructions\ninclude Makefile.api' Makefile
```

Now run
```
SEARCH_DIR=<path_to_crds_or_type.go> make api-docs-path
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
   curl -o .github/workflows/generate-api-docs-release-2.14.yml https://raw.githubusercontent.com/jnpacker/api-documentation/refs/heads/main/.github/workflows/generate-api-docs-release-2.14.yml
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

1. **Clone the main branch of the repository:**
   ```sh
   git clone https://github.com/stolostron/api-documents.git
   cd api-documents
   git checkout main
   ```

2. **Create and checkout a new branch for the release:**
   Replace `release-2.15.0` with your desired release branch name.
   ```sh
   git checkout -b release-2.15
   ```

3. **Copy the existing workflow to the new release version:**
   ```sh
   cp .github/workflows/generate-api-docs-release-2.14.yml .github/workflows/generate-api-docs-release-2.15.yml
   ```

4. **Edit the new workflow file:**
   - Open `.github/workflows/generate-api-docs-release-2.15.yml` in your editor.
   - Update the `RELEASE_BRANCH` and `BACKPLANE_BRANCH` environment variables to match your new release. For example:
     ```yaml
     env:
       RELEASE_BRANCH: 'release-2.15.0'
       BACKPLANE_BRANCH: 'backplane-2.10.0'
     ```
   - Optionally, update the workflow `name:` at the top for clarity.
   - Make sure the release version matches the current release branch you are working on.

5. **Commit and push your changes:**
   ```sh
   git add .github/workflows/generate-api-docs-release-2.15.yml
   git commit -m "chore: add API docs workflow for release-2.15"
   git push origin release-2.15
   ```

6. **Merge the change back to main:**
   - Switch back to the `main` branch:
     ```sh
     git checkout main
     ```
   - Merge the release branch:
     ```sh
     git merge release-2.15
     ```
   - Push the updated `main` branch:
     ```sh
     git push origin main
     ```

Once the workflow is committed to your default branch, the APIs will start to be generated daily automatically.

This ensures the new GitHub Action workflow is available and will be used for the new release branch.
