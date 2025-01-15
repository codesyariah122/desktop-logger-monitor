#### Python 3 compatibility

- Build

```
pyinstaller --onefile --windowed activity_monitor.py
```

**On Mac**

```
pyinstaller --add-data "assets;assets" --add-data "data;data" --onefile activity-monitor.py
```

**On Windows**

```
pyinstaller --add-data "assets;assets" --add-data "data;data" --onefile activity-monitor.py
```
