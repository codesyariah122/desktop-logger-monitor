#### Python 3.10.9 compatibility

- Insalling requirements

```
pip install -r requirements.txt
```

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
python -m PyInstaller --noconsole  --add-data "assets;assets" --add-data ".env;." --add-data "data;data" --hidden-import=requests --onefile activity-monitor.py --exclude PyQt5
```

_On Mac_

```
python -m PyInstaller --noconsole --add-data "assets:assets" --add-data ".env:." --add-data "data:data" --hidden-import=requests --onefile activity-monitor.py --exclude PyQt5 --no-codesign
```
