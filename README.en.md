# Pip GUI

Cross-platform graphical Pip manager — manage Python packages without typing commands.

> [中文文档](./README.md)

## Features

- Graphical UI to install, uninstall, query, and upgrade with one click
- Real-time pip output in a live log panel
- Works on Windows / macOS / Linux
- Comes with one-click dependency installers — no manual setup required

## Release Assets

| File | Platform | Description |
|--------|--------|------|
| `InstallDependencies.bat` | Windows | Windows one-click dependency installer |
| `install_dependencies.sh` | macOS / Linux | macOS & Linux dependency installer |
| `Pip-GUI-v0.1-macos.dmg` | macOS | Standard Mac installer — drag to Applications |
| `Pip-GUI-v0.1-linuxormacos.zip` | macOS / Linux | Portable archive — extract and run |
| `Pip-GUI-windows-portable.exe` | Windows | Portable single-file Windows build |
| `Pip-GUI-windows-setup.exe` | Windows | 7-Zip self-extracting installer |

## Usage

### Option 1: Run the packaged binaries

1. Go to the repository's [Releases](../../releases) page and download the file for your system.
2. Run it:
- **Windows portable**: double-click `Pip-GUI-windows-portable.exe`
- **Windows installer**: double-click `Pip-GUI-windows-setup.exe`, choose an install path, and click Install
- **macOS DMG**: open the image and drag the app into **Applications**
- **macOS / Linux archive**: extract and run the included executable

### Option 2: Run from source

1. Download the source code.
2. Install dependencies:
- **Windows**: double-click `InstallDependencies.bat`
- **macOS / Linux** in a terminal:
```bash
chmod +x install_dependencies.sh
./install_dependencies.sh
```
3. Launch the program:
```bash
python main.py
```

## Notes

1. Python must be installed and added to your system `PATH` first.
2. On macOS / Linux, remember to grant execute permission to the shell script before running.
3. The Windows installer does not create a desktop shortcut.

## Project Info

- Name: Pip GUI
- Series: QPALZM Toolkit
- Author: AdkSetup
- Supported platforms: Windows / macOS / Linux

## License

Released under the [MIT License](./LICENSE).
