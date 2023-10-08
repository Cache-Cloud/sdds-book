import os

def find_md_files(directory):
    md_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    return md_files

def generate_md_tree(directory):
    with open('md.md', 'w', encoding='utf-8') as md_file:
        for root, dirs, files in os.walk(directory):
            for dir in dirs:
                dir_path = os.path.join(root, dir)
                relative_dir_path = os.path.relpath(dir_path, directory)
                md_file.write(f"* [{dir}]({dir}.md)\n")
                md_files = find_md_files(dir_path)
                for md_file_path in md_files:
                    relative_md_path = os.path.relpath(md_file_path, directory)
                    md_file.write(f"  * [{os.path.basename(md_file_path)}]({relative_md_path})\n")

if __name__ == '__main__':
    current_directory = os.getcwd()
    generate_md_tree(current_directory)
