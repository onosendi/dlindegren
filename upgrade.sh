#!/bin/bash

# Change directory to this script's location.
cd "$(dirname "$0")"

# Remove existing node modules.
NODE_MODULES="$(pwd -P)/node_modules"
if [ -d "$NODE_MODULES" ]; then
  COMMAND="rm -rf ${NODE_MODULES}"
  echo ""
  echo "Removing old node modules..."
  echo""
  eval $COMMAND
fi

# Remove existing parcel cache.
PARCEL_CACHE="$(pwd -P)/.parcel-cache"
if [ -d "$PARCEL_CACHE" ]; then
  COMMAND="rm -rf ${PARCEL_CACHE}"
  echo ""
  echo "Removing old parcel cache..."
  echo""
  eval $COMMAND
fi

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
