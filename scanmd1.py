import os

def list_md_files(directory):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                md_files.append(os.path.join(root, file))
    return md_files

def generate_directory_tree(md_files):
    tree = ""
    for md_file in sorted(md_files):
        relative_path = os.path.relpath(md_file, start=os.getcwd())
        depth = relative_path.count(os.sep)
        indentation = "    " * depth
        tree += f"{indentation}- [{os.path.basename(md_file)}]({relative_path})\n"
    return tree

def main():
    current_directory = os.getcwd()
    md_files = list_md_files(current_directory)
    directory_tree = generate_directory_tree(md_files)

    with open("md.md", "w", encoding="utf-8") as md_file:
        md_file.write(directory_tree)

if __name__ == "__main__":
    main()
