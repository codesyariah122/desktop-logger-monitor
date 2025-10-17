#### Python 3.10.9 compatibility
<img width="502" height="366" alt="Screenshot 2025-10-17 130231" src="https://github.com/user-attachments/assets/6454f584-a5f8-418d-b099-b47cf4d2b3c3" />
<img width="1917" height="1018" alt="Screenshot 2025-10-17 130245" src="https://github.com/user-attachments/assets/472a50ee-ba5a-4896-a838-8874b26e130a" />


Uploading preview-desktop-logger-monitor.mp4…


- Insalling requirements

```
pip install -r requirements.txt
```

- Compiling
Inno Setup Compiler 6.4.0

- Build

**On Mac**

```
pyinstaller --add-data "assets;assets" --add-data "data;data" --onefile activity-monitor.py
```

**On Windows**

```
pyinstaller --add-data "assets;assets" --add-data "data;data" --onefile activity-monitor.py
```

### Clean Build

```
pyinstaller --clean --add-data "assets;assets" --add-data "data;data" --hidden-import=requests --onefile activity-monitor.py
```

### Use venv

```
python -m venv venv
source venv/bin/activate  # Aktifkan venv di Linux/macOS
venv\Scripts\activate     # Aktifkan venv di Windows
pip install PySide2 pyinstaller requests pyautogui keyboard
python -m PyInstaller --add-data "assets;assets" --add-data "data;data" --hidden-import=requests --onefile activity-monitor.py
```

### Using exclude

```
python -m PyInstaller  --add-data "assets;assets" --add-data "data;data" --hidden-import=requests --onefile activity-monitor.py --exclude PyQt5
```

### No Console

```
python -m PyInstaller --windowed --noconsole  --add-data "assets;assets" --add-data ".env;." --add-data "data;data" --hidden-import=requests --onefile activity-monitor.py --exclude PyQt5
```

_On Mac_

```
pip install numpy cryptography pyperclip pyautogui platformdirs requests ipython
```

```
python -m PyInstaller --noconsole --add-data "assets:assets" --add-data ".env:." --add-data "data:data" --hidden-import=requests --onefile activity-monitor.py --exclude PyQt5 --osx-bundle-identifier com.yourcompany.activitymonitor
```

_OR_

```
python -m PyInstaller --hidden-import=pkg_resources._vendor.jaraco.functools \
                      --hidden-import=pkg_resources._vendor.jaraco.context \
                      --hidden-import=pkg_resources._vendor.jaraco.text \
                      --hidden-import=shiboken2 \
                      --noconsole --add-data "assets:assets" --add-data ".env:." --add-data "data:data" \
                      --onefile activity-monitor.py

pyinstaller --onefile --windowed --noconsole --icon=assets/fav-1-1.png activity-monitor.py

pyinstaller --exclude-module=winreg --exclude-module=nt --exclude-module=psutil --exclude-module=cryptography --exclude-module=org --onefile --windowed --noconsole --icon=assets/fav-1-1.png activity-monitor.py

codesign --sign "Developer ID Application: <Your Developer Name>" --timestamp --deep --force dist/activity-monitor.app
```

#### Reforce for change python version
```
# pastikan kamu ada di folder project
cd "C:\Users\Laptop Store 95\puji-project\python-project"

# hapus venv lama
rmdir venv -Recurse -Force

# buat ulang venv dengan Python baru
python -m venv venv

# aktifkan
.\venv\Scripts\Activate.ps1

# upgrade pip
python -m pip install --upgrade pip
```

4️⃣ Upgrade pip & setuptools
```
python -m pip install --upgrade pip setuptools
```

5️⃣ Install semua package dari requirements.txt
```
pip cache purge
pip install -r requirements.txt
```


⚠️ Catatan penting:
Kamu punya duplikat PySide2==5.15.2.1 di requirements.txt.
Kamu bisa hapus salah satunya supaya tidak warning:

PySide2==5.15.2.1

6️⃣ Jalankan proyek kamu lagi
```
python activity-monitor.py
```

Kalau environment sudah benar, tidak akan muncul error seperti:

No Python at "C:\Users\Laptop Store 95\AppData\Local\Programs\Python\Python310\python.exe"

💡 Opsional (buat otomatis sekali jalan)

Kalau kamu mau biar proses ini otomatis dan cepat, buat file reset_venv.ps1 di root project dengan isi ini:
```
Write-Host "=== Reset Virtual Environment ==="
if (Test-Path "venv") {
    Remove-Item "venv" -Recurse -Force
    Write-Host "Old venv deleted."
}

python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools
pip install -r requirements.txt

Write-Host "`n=== Done! Virtual environment ready. ==="
```

Lalu jalankan:
```
.\reset_venv.ps1
```  
