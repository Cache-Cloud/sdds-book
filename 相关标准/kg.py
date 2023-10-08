from pathlib import Path

def rename_files():
    for file in Path(".").iterdir():
        if file.is_file():
            new_name = file.name.replace("　", "").replace("∕", "")
            if new_name != file.name:
                file.rename(new_name)

rename_files()