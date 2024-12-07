# Save the git repo path
GIT_REPO_DIRECTORY=$(dirname "$0")

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
SCRIPT_PATH=$(dirname "$SCRIPT")

TEMP_REPO_PATH="$(dirname "$SCRIPT")/tmp/site"

mkdir "$(dirname "$SCRIPT")/tmp/"
mkdir $TEMP_REPO_PATH

# Upload the English terms
python -m src.cli docs/TERMS_EN.md $TEMP_REPO_PATH/terms.pdf

# Copy the CNAME file to the directory
cp "$SCRIPT_PATH/src/CNAME" $TEMP_REPO_PATH