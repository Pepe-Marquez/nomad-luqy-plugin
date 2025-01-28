#!/bin/sh

if ! command -v rsync >/dev/null 2>&1; then
  echo "rsync required, but not installed!"
  exit 1
else
  rsync -avh nomad-luqy-plugin/ .
  rm -rfv fnomad-luqy-plugin
fi
