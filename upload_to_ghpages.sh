GHPAGE_REPO_SSHLINK="git@github.com:basvandriel/legal-pdf-microservice-gh-pages.git"

# Save the git repo path
GIT_REPO_DIRECTORY=$(dirname "$0")

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

TEMP_REPO_PATH="$(dirname "$SCRIPT")/tmp/legal-pdf-microservice-gh-pages"

mkdir "$(dirname "$SCRIPT")/tmp/"
mkdir $TEMP_REPO_PATH

# Upload the English terms
python -m src.cli docs/TERMS_EN.md $TEMP_REPO_PATH/terms.pdf

# Copy the CNAME file to the directory
cp "$SCRIPT_PATH/src/CNAME" $TEMP_REPO_PATH

# Initialize the temporary repository
git init $TEMP_REPO_PATH

# # Add the remote
git -C $TEMP_REPO_PATH remote add origin $GHPAGE_REPO_SSHLINK

TARGET_BRANCH="main"

git -C "$TEMP_REPO_PATH" checkout -B "$TARGET_BRANCH"

# # Stage all the files and commit
git -C $TEMP_REPO_PATH add .
git -C $TEMP_REPO_PATH commit -m "Update legal terms"

# # Force push, ensuring we only have one commit
git -C $TEMP_REPO_PATH push --set-upstream origin "$TARGET_BRANCH" --force

echo "Succesfully pushed code to repository"

# Clean up
rm -fr $TEMP_REPO_PATH