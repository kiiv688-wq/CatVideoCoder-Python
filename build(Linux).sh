#!/bin/bash
set -e
echo "🐧 Compiling for Linux..."
# Перевірка залежностей
if ! command -v patchelf &> /dev/null; then
    echo "⚠️ patchelf not found. Install: sudo apt install patchelf"
    exit 1
fi
nuitka --standalone --onefile \
  --windows-icon-from-ico="favicon.ico" \
  --windows-console-mode=disable \
  --product-name="CatVideoCoder" \
  --file-description="CatVideoCoder" \
  --include-package=gi \
  --include-package=gi.repository \
  --include-package-data=gi \
  --follow-import-to=gi \
  --follow-import-to=gi.repository \
  main.py
mv main.bin CatVideoCoder-Linux
echo "✅ Done: CatVideoCoder-Linux"