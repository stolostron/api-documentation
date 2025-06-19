## Development
### How to use this with an indvidual repository.
Check out the repository, then run the following commnad:
```
curl -o Makefile.api https://raw.githubusercontent.com/stolostron/api-documentation/main/Makefile && \
curl -o cmd/generate-api-docs.py https://raw.githubusercontent.com/stolostron/api-documentation/main/cmd/gen-api-docs.py && \
sed -i '1i include Makefile.api' Makefile
```

### How to add a new release

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
   git checkout -b release-2.15.0
   ```

3. **Copy and rename the GitHub Action workflow:**
   ```sh
   cp .github/workflows/generate-api-docs-release-2.14.yml .github/workflows/generate-api-docs-release-2.15.yml
   ```

4. **Edit the new workflow file:**
   - Open `.github/workflows/generate-api-docs-release-2.15.0.yml` in your editor.
   - Update the `RELEASE_BRANCH` and `BACKPLANE_BRANCH` environment variables to match your new release. For example:
     ```yaml
     env:
       RELEASE_BRANCH: 'release-2.15.0'
       BACKPLANE_BRANCH: 'backplane-2.10.0'
     ```
   - Optionally, update the workflow `name:` at the top for clarity.

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
     git merge release-2.15.0
     ```
   - Push the updated `main` branch:
     ```sh
     git push origin main
     ```

This ensures the new GitHub Action workflow is available and will be used for the new release branch.
