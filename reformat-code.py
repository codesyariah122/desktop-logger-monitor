# @author Puji Ermanto <pujiermanto@gmail>
# @return refactor
# @author Puji Ermanto
# @return refactor

import os
import re

# Path file asli dan folder output
source_file = "activity-monitor.py"
output_folder = "modules"

# Membuat folder output jika belum ada
os.makedirs(output_folder, exist_ok=True)

# Membaca isi file asli
with open(source_file, "r", encoding="utf-8") as file:
    code = file.read()

# Regex untuk menemukan semua kelas
class_pattern = re.compile(
    r"^(class\s+\w+.*?:\s*\n(?:\s+.*\n)*)",
    re.MULTILINE | re.DOTALL
)
classes = class_pattern.findall(code)

# Memisahkan setiap kelas ke dalam file terpisah
for class_code in classes:
    print(f"Found class:\n{class_code}\n{'-'*40}")
    # Mendapatkan nama kelas
    class_name_match = re.match(r"class\s+(\w+)", class_code)
        
    if class_name_match:
        class_name = class_name_match.group(1)
        # Menentukan nama file berdasarkan nama kelas
        file_name = f"{class_name}.py"  # Nama file berdasarkan nama kelas
        file_path = os.path.join(output_folder, file_name)
        
        # Menyimpan kelas ke dalam file
        with open(file_path, "w", encoding="utf-8") as class_file:
            class_file.write(f"# {class_name} class\n\n")
            class_file.write(class_code)
        print(f"Class {class_name} saved to {file_path}")
