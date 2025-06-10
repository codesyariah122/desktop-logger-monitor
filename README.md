# Preview
![ezyZip-ezgif com-video-to-gif-converter](https://github.com/user-attachments/assets/7532bc9f-745a-488c-92f6-b364832d03a1)



### Python 3.10.9 compatibility

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
