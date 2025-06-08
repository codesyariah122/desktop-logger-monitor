from setuptools import setup

APP = ['activity-monitor.py']
DATA_FILES = ['assets', 'data']
OPTIONS = {
    'argv_emulation': True,
    'packages': ['requests', 'pyautogui', 'keyboard', 'PySide2'],
    'includes': ['pyautogui', 'keyboard', 'requests', 'platform', 'threading', 'time', 'json', 'sys'],
    'plist': {
        'CFBundleName': 'Activity Monitor',
        'CFBundleDisplayName': 'Activity Monitor PM Tokoweb',
        'CFBundleIdentifier': 'com.tokoweb.activitymonitor',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
    }
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
