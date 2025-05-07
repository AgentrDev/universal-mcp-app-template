#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# Get the project slug which is the folder name relative to the output directory
APP_NAME="{{ cookiecutter.app_name.lower() }}"
ORG_NAME="universal-mcp" # Organization name
# REPO_NAME will be universal-mcp-<app_name> based on cookiecutter.json
REPO_NAME="${APP_NAME}"
BRANCH_NAME="master" # Desired initial branch name

echo "Initializing git repository in $APP_NAME..."

# Initialize a new Git repository
git init

# Add all files
git add .

# Make the initial commit
git commit -m "feat: Initial commit from MCP CLI init command"

echo "Creating GitHub repository ${ORG_NAME}/${REPO_NAME} as private and setting it as the origin remote..."
echo "Note: Files will NOT be pushed automatically. You will need to run 'git push' manually later."

# Create the private GitHub repository and set the remote, but DO NOT push
# Assumes gh CLI is installed and authenticated
# # Using --source . links the current directory to the new repo and automatically sets the origin remote
gh repo create "${ORG_NAME}/${REPO_NAME}" --private --source . --remote origin

# # Rename the default branch to master locally if it's currently 'main'
# # Check if the current branch is 'main' and rename it to 'master'
# CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
# if [ "$CURRENT_BRANCH" = "main" ]; then
#     echo "Renaming local branch 'main' to '$BRANCH_NAME'..."
#     git branch -M "$BRANCH_NAME"
# fi

# echo "GitHub repository created and remote 'origin' set successfully."
# echo "You can now make changes, commit, and push using 'git push -u origin master'."
