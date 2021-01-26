#!/bin/bash

# Change directory to this script's location.
cd "$(dirname "$0")"

# Install NPM packages.
COMMAND="npm install"
echo ""
echo "Installing NPM packages ($COMMAND)..."
echo ""
eval $COMMAND || exit 1

# Build NPM assets.
COMMAND="npm run build"
echo ""
echo "Building NPM assets ($COMMAND)..."
echo ""
eval $COMMAND || exit 1

exit 0
