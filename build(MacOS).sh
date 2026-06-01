#!/bin/bash
set -e
echo "🍎 Compiling for macOS..."
pip install -r requirements.txt
nuitka --standalone --macos-create-app-bundle \
  --macos-app-icon="favicon.icns" \
  --macos-app-name="CatVideoCoder" \
  --product-name="CatVideoCoder" \
  --include-package=gi \
  --include-package=gi.repository \
  --include-package-data=gi \
  --follow-import-to=gi \
  --follow-import-to=gi.repository \
  main.py
mv main.app CatVideoCoder-macOS.app
codesign --deep --force --sign - "CatVideoCoder.app"
echo "✅ Done: CatVideoCoder-macOS.app"