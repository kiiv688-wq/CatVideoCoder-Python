# 🎬 CatVideoCoder
> YouTube to DaVinci Resolve Converter

A lightweight GTK4 application for downloading YouTube videos and converting them into editing-optimized formats for seamless workflow in DaVinci Resolve.

---

## ⚠️ Important Notice
This program **does not save configuration**. Each time you run it, you must manually select:
- 📁 Output directory
- 🎞️ Format: Video / Audio Only / No Audio
- 📐 Resolution: 1080p / 1440p / 2160p
- 🎨 Codec: ProRes / DNxHR / MKV (AV1)

---

## 🛠 System Requirements

| Component | Requirement |
|-----------|-------------|
| **Python** | 3.10 or higher |
| **ffmpeg** | Must be in `PATH` or in the same directory as the executable |
| **yt-dlp** | Must be in `PATH` or in the same directory as the executable |
| **GTK4** | Installed via system package manager (see instructions below) |

---

🚀 Building from Source
Quick Start
# 1. Clone repository
git clone https://github.com/kiiv688-wq/CatVideoCoder-Python.git
cd CatVideoCoder-Pyhton

# 2. Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run build script for your platform
# Linux:
chmod +x "build(Linux).sh" && ./build(Linux).sh

# macOS:
chmod +x "build(MacOS).sh" && ./build(MacOS).sh

# Windows:
build.bat

---

## 📦 Installation

### 🔹 Recommended: Use a Virtual Environment
```bash
python -m venv .venv

# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate

🔹 Install Python Dependencies

🐧 Linux
Arch / EndeavourOS / CachyOS / Prism Linux

# Update system and install GTK4 dependencies
sudo pacman -Syu gtk4 cairo

# Install stable patchelf (v0.18.0 has known bugs with Nuitka)
sudo pacman -U https://archive.archlinux.org/packages/p/patchelf/patchelf-0.17.2-1-x86_64.pkg.tar.zst

# Make build script executable and run
chmod +x "build(Linux).sh"
./"build(Linux).sh"

Debian / Ubuntu / Linux Mint

# Install GTK4 dependencies
sudo apt update && sudo apt install -y libgtk-4-dev libcairo2-dev patchelf

# Make build script executable and run
chmod +x "build(Linux).sh"
./"build(Linux).sh"

🍎 macOS

# Install GTK4 and build tools via Homebrew
brew install gtk4 pkg-config cairo

# Make build script executable and run
chmod +x "build(MacOS).sh"
./"build(MacOS).sh"

🪟 Windows
Prerequisites
MSYS2 with MinGW64 environment
pip install -r requirements.tx

---
❓ Troubleshooting

 | Error/Issue | Solution |
 |-------------------------------------------|-------------------------------------------------------------------------------------------------|
 | ModuleNotFoundError: No module named 'gi' | Install PyGObject: pip install PyGObject. On Linux, ensure libgirepository1.0-dev is installed. |
 |patchelf version 0.18.0 is a known buggy release|Downgrade to patchelf==0.17.2 (see Arch instructions above).|
 |libgtk-4.so not found or similar GTK errors| Install GTK4 runtime: sudo apt install libgtk-4-1 (Debian) or sudo pacman -S gtk4 (Arch).|
 |Program crashes on Windows startup | Ensure ffmpeg.exe and yt-dlp.exe are in PATH or in the same folder as the .exe.|
 |Icon not displaying on Linux | Convert icon to PNG: convert favicon.ico favicon.png and update --linux-icon flag in build script.|
 |FATAL: Error, unknown plug-in 'gtk' referenced | Remove --enable-plugins=gtk from Nuitka command — GTK support is built-in, no plugin needed. |
 