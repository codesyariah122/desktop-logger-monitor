# Preview
[![Watch the video](https://img.youtube.com/vi/HyQbqRQ3CRQ/maxresdefault.jpg)](https://youtu.be/HyQbqRQ3CRQ)

Proyek ini adalah aplikasi pemantauan aktivitas yang ditulis dalam Python menggunakan PySide2 untuk antarmuka pengguna grafis (GUI). Aplikasi ini dirancang untuk memantau penggunaan aplikasi, aktivitas keyboard, dan mouse, serta mengumpulkan data pengguna berdasarkan email yang dimasukkan.

Fitur Utama:

    Antarmuka Pengguna:
        Menggunakan PySide2 untuk membuat GUI yang responsif.
        Menampilkan aplikasi aktif dan waktu penggunaannya dalam tabel.
        Menampilkan penggunaan keyboard dan mouse dalam persentase.

    Pemantauan Aktivitas:
        Mencatat aplikasi yang sedang aktif dan waktu yang dihabiskan di setiap aplikasi.
        Menghitung jumlah peristiwa keyboard dan mouse.

    Pengelolaan Email:
        Meminta pengguna untuk memasukkan email yang terdaftar.
        Memeriksa validitas email melalui API.
        Mengambil data pengguna dari API berdasarkan email yang dimasukkan.

    Penyimpanan Data:
        Menyimpan data aktivitas ke dalam file JSON.
        Mengirim data ke server menggunakan API.

    Tray Icon:

        Menyediakan ikon sistem tray untuk akses cepat.

        Menyembunyikan aplikasi ke tray alih-alih menutupnya.

Struktur Kode:

    Import Library:
        Mengimpor berbagai modul seperti os, requests, json, PySide2, dan lainnya untuk fungsionalitas yang diperlukan.

    Fungsi resource_path:
        Mengelola jalur sumber daya untuk file yang diperlukan oleh aplikasi.

    Kelas EmailDialog:
        Menangani dialog untuk memasukkan email pengguna.
        Memuat email dari file jika tersedia.

    Kelas ActivityMonitorApp:
        Kelas utama untuk aplikasi pemantauan aktivitas.
        Mengatur antarmuka pengguna, pemantauan aktivitas, dan pengelolaan data.

    Fungsi Pemantauan:
        Menggunakan thread untuk memantau peristiwa keyboard dan mouse secara bersamaan.
        Mengupdate penggunaan aplikasi dan aktivitas pengguna secara berkala.

    Fungsi Penyimpanan dan Pengiriman Data:

        Menyimpan data ke file JSON dan mengirim data ke server menggunakan API.

Kesimpulan:

Proyek ini adalah aplikasi yang berguna untuk memantau dan menganalisis penggunaan waktu di berbagai aplikasi, serta memberikan wawasan tentang aktivitas pengguna. Dengan antarmuka yang intuitif dan fungsionalitas yang kuat, aplikasi ini dapat membantu pengguna untuk lebih produktif dan sadar akan penggunaan waktu mereka.

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

[![Buy Me Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/codesyariah122)
