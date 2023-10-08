# 导入os模块，用于操作文件和目录
import os

# 定义一个函数，用于递归地遍历目录下的所有pdf文件
def scan_pdf_files(dir_path):
    # 获取目录下的所有文件和子目录
    files_and_dirs = os.listdir(dir_path)
    # 遍历每个文件或子目录
    for f in files_and_dirs:
        # 拼接完整的路径
        f_path = os.path.join(dir_path, f)
        # 判断是否是文件
        if os.path.isfile(f_path):
            # 判断是否是pdf文件
            if f_path.endswith(".pdf"):
                # 获取pdf文件的名称（不含扩展名）
                pdf_name = os.path.splitext(f)[0]
                # 创建同名的.md文件
                md_file = pdf_name + ".md"
                # 打开.md文件，以写入模式
                with open(os.path.join(dir_path, md_file), "w") as f:
                    # 写入<iframe>标签，用于嵌入pdf文件
                    f.write(f'<iframe src="https://mozilla.github.io/pdf.js/web/viewer.html?file=https://xiaochao.kutina.cn/{os.path.relpath(f_path)}" width="100%" height=1000px></iframe>')
        # 判断是否是子目录
        elif os.path.isdir(f_path):
            # 递归地遍历子目录下的所有pdf文件
            scan_pdf_files(f_path)

# 获取当前目录的路径
current_dir = os.getcwd()

# 调用函数，扫描当前目录及所有子目录下的所有pdf文件
scan_pdf_files(current_dir)
