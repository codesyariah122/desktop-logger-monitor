import tkinter as tk
from tkinter import messagebox

# Fungsi untuk tombol
def on_button_click():
    message = entry.get()
    if message:
        messagebox.showinfo("Info", f"Anda mengetik: {message}")
    else:
        messagebox.showwarning("Peringatan", "Masukkan teks terlebih dahulu!")

# Membuat jendela utama
root = tk.Tk()
root.title("Program GUI Sederhana")

# Ukuran jendela
root.geometry("300x200")

# Label
label = tk.Label(root, text="Masukkan sesuatu:", font=("Arial", 12))
label.pack(pady=10)

# Kotak teks
entry = tk.Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)

# Tombol
button = tk.Button(root, text="Klik Saya", font=("Arial", 12), bg="blue", fg="white", command=on_button_click)
button.pack(pady=20)

# Menjalankan aplikasi
root.mainloop()
