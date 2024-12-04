GHPAGE_REPO_SSHLINK="git@github.com:basvandriel/legal-pdf-microservice-gh-pages.git"


# TODO build the terms file in ghpage

# Save the git repo path
GIT_REPO_DIRECTORY=$(dirname "$0")

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")

# Get the path to the repository
GIT_REPO_PATH="$(dirname "$SCRIPT")/data/ghpages"

# Remove the old repository
rm -fr $GIT_REPO_PATH/.git

# Initialize the temporary repository
git init $GIT_REPO_PATH

# Add the remote
git -C $GIT_REPO_PATH remote add origin $GHPAGE_REPO_SSHLINK

# Stage all the files and commit
git -C $GIT_REPO_PATH add .
git -C $GIT_REPO_PATH commit -m "Update legal terms"

# Force push, ensuring we only have one commit
git -C $GIT_REPO_PATH push --set-upstream origin main --force