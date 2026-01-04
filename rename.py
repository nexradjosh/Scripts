import os
import math
import sys

def rename_files(folder_path):
    folder_path = os.path.abspath(folder_path)
    folder_name = os.path.basename(folder_path)

    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f))
    ]

    files.sort()

    total = len(files)
    if total == 0:
        print("No files to rename.")
        return

    pad = max(2, int(math.log10(total)) + 1)

    for i, filename in enumerate(files, start=1):
        old = os.path.join(folder_path, filename)
        _, ext = os.path.splitext(filename)
        new = os.path.join(
            folder_path,
            f"{folder_name}_{str(i).zfill(pad)}{ext}"
        )
        os.rename(old, new)

    print(f"Renamed {total} files in {folder_name}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 rename.py <folder>")
        sys.exit(1)

    rename_files(sys.argv[1])
