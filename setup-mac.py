import subprocess
import sys
import os

try:
    import PyInstaller
except ImportError:
    print("PyInstaller tidak terpasang. Install terlebih dahulu dengan 'pip install pyinstaller'.")
    sys.exit(1)

script_path = "activity-monitor.py"

icon_path = "assets/fav-1-1.png"

if not os.path.exists(script_path):
    print(f"File {script_path} tidak ditemukan!")
    sys.exit(1)

if not os.path.exists(icon_path):
    print(f"Icon {icon_path} tidak ditemukan!")
    sys.exit(1)

cmd = [
    "pyinstaller",
    "--onefile",
    "--windowed",
    "--noconsole",
    f"--icon={icon_path}",
    script_path
]

print("Membangun executable dengan PyInstaller...")
subprocess.run(cmd)

print("Proses build selesai!")
