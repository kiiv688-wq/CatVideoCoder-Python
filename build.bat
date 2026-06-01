@echo off
echo 🪟 Compiling for Windows...
pip install -r requirements.txt
nuitka --standalone --onefile ^
  --windows-icon-from-ico="favicon.ico" ^
  --windows-console-mode=disable ^
  --product-name="CatVideoCoder" ^
  --file-description="CatVideoCoder" ^
  --include-package=gi ^
  --include-package=gi.repository ^
  --include-package-data=gi ^
  --follow-import-to=gi ^
  --follow-import-to=gi.repository ^
  main.py
move main.exe CatVideoCoder-Windows.exe
echo ✅ Done: CatVideoCoder-Windows.exe
pause