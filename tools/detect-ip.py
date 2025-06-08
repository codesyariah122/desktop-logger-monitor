import socket

def scan_network(port=9100):
    printers = []
    for i in range(1, 255):  # Scan 192.168.1.1 - 192.168.1.254
        ip = f"192.168.1.{i}"
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)  # Timeout 0.5 detik
                if s.connect_ex((ip, port)) == 0:
                    printers.append(ip)
                    print(f"Printer ditemukan di IP: {ip}")
        except Exception:
            continue
    return printers

if __name__ == "__main__":
    printers = scan_network()
    if printers:
        print("Printer yang ditemukan:", printers)
    else:
        print("Tidak ada printer yang ditemukan.")
