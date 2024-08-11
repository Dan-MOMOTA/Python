import fileinput

def search_replace_in_files(dir_path, search_text, replace_text):
    #inplace=True 参数表示在原始文件上进行操作
    for line in fileinput.input([f"{dir_path}/*"], inplace=True):
        #end=''是为了避免print()函数在输出时添加额外的换行符
        print(line.replace(search_text, replace_text), end='')

# 使用示例：
search_replace_in_files('/path/to/files', 'old_text', 'new_text')