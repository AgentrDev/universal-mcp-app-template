#!/bin/bash

# Script to push the local project '{{ cookiecutter.project_slug }}' to the 'AgentrDev' GitHub organization.
# Requires GitHub CLI (gh) to be installed and authenticated with access to the organization.

# --- Configuration ---
ORG_NAME="AgentrDev"
REPO_NAME="universal-mcp-{{ cookiecutter.package_name }}"
VISIBILITY="private" # Or 'public' or 'internal' as needed

# --- Script ---

echo "Navigating to project directory..."
PROJECT_ROOT="$(pwd)"
echo "Project root: $PROJECT_ROOT"

# Check if Git is initialized, if not, initialize it
if [ ! -d "$PROJECT_ROOT/.git" ]; then
  echo "Initializing Git repository..."
  git init
  if [ $? -ne 0 ]; then echo "Error: git init failed. Exiting."; exit 1; fi
else
  echo "Git repository already initialized."
fi

# Add all files and commit (initial commit message)
echo "Adding files and creating initial commit..."
git add .
git commit -m "Initial commit of {{ cookiecutter.app_name }} project"
if [ $? -eq 0 ]; then
    echo "Commit successful."
elif [ $? -eq 1 ]; then
    echo "Warning: No changes to commit. Continuing..."
else
    echo "Error: git commit failed. Exiting."; exit 1;
fi

# Check if the remote 'origin' already exists
if git remote add origin https://github.com/$ORG_NAME/$REPO_NAME 2>/dev/null; then
  echo "Remote 'origin' added."
else
  echo "Remote 'origin' already exists or failed to add. Proceeding with push."
  CURRENT_REMOTE=$(git remote get-url origin)
  EXPECTED_REMOTE="https://github.com/$ORG_NAME/$REPO_NAME"
  if [ "$CURRENT_REMOTE" != "$EXPECTED_REMOTE" ] && [ "$CURRENT_REMOTE" != "git@github.com:$ORG_NAME/$REPO_NAME.git" ]; then
    echo "Warning: Existing remote 'origin' URL ($CURRENT_REMOTE) does not match the expected URL ($EXPECTED_REMOTE)."
    echo "Attempting to remove existing remote and add the correct one..."
    git remote remove origin
    if [ $? -ne 0 ]; then echo "Error: Failed to remove existing remote. Exiting."; exit 1; fi
    git remote add origin https://github.com/$ORG_NAME/$REPO_NAME
    if [ $? -ne 0 ]; then echo "Error: Failed to add correct remote after removal. Exiting."; exit 1; fi
    echo "Remote 'origin' updated."
  fi
fi

# Create the repository in the organization using gh CLI and push
echo "Creating '$REPO_NAME' repo in '$ORG_NAME' with visibility '$VISIBILITY' on GitHub..."
gh repo create "$ORG_NAME/$REPO_NAME" --$VISIBILITY --confirm --clone=false

GH_EXIT_CODE=$?
if [ $GH_EXIT_CODE -eq 0 ]; then
    echo "Repository '$ORG_NAME/$REPO_NAME' created or already exists."
elif [ $GH_EXIT_CODE -ne 0 ]; then
    echo "Error: gh repo create failed with exit code $GH_EXIT_CODE. Ensure you are authenticated and have permissions."
    exit 1
fi

# Push the local code to the remote repository
echo "Pushing local code to remote repository..."
git push -u origin master
if [ $? -ne 0 ]; then
    echo "Error: git push failed. Ensure the remote 'origin' is correct and you have push permissions."
    exit 1
fi

echo ""
echo "----------------------------------------------------"
echo "Process completed successfully!"
echo "Your project should now be available at https://github.com/$ORG_NAME/$REPO_NAME"
echo "----------------------------------------------------"
