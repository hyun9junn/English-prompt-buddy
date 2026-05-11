#!/bin/bash
set -e

REPO="https://github.com/hyun9junn/English-prompt-buddy.git"
SKILL="english-prompt-buddy"
TMP_DIR=$(mktemp -d)

cleanup() {
  rm -rf "$TMP_DIR"
}
trap cleanup EXIT

echo "Cloning English Prompt Buddy..."
git clone "$REPO" "$TMP_DIR" --depth 1 --quiet

if [ "$1" = "--project" ]; then
  DEST=".claude/skills"
  mkdir -p "$DEST"
  rm -rf "$DEST/$SKILL"
  cp -R "$TMP_DIR/$SKILL" "$DEST/"
  echo "Installed to .claude/skills/$SKILL (project-specific)"
else
  DEST="$HOME/.claude/skills"
  mkdir -p "$DEST"
  rm -rf "$DEST/$SKILL"
  cp -R "$TMP_DIR/$SKILL" "$DEST/"
  echo "Installed to ~/.claude/skills/$SKILL (global)"
fi

echo "Done! Restart Claude Code and say 'hey buddy' to activate."
