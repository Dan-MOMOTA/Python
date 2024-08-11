import os
import re

def batch_rename(path, prefix='', suffix=''):
    # 获取指定文件夹下的所有文件
    #a = os.listdir(path)
    #print(a)

    for i, filename in enumerate(os.listdir(path)):
        #print(i,filename)
        # i:03d是一个格式规范，表示将变量i格式化为一个3位数的整数，不足3位时在前面补0
        #print(f"{i:03d}")
        #print(f"{os.path.splitext(filename)[1]}")
        # 匹配_后获取后面的数据
        back_name = re.search('_(w+)',os.path.splitext(filename)[0]).group(1)
        print(back_name)
        # {}是格式化字符串的占位符，用于插入变量或表达式的值
        # f是格式化字符串的前缀，表示这是一个f-string，可以在字符串中直接使用变量
        #os.path.splitext()函数 作用：将文件名和扩展名分开
        new_name = f"{prefix}{back_name}{os.path.splitext(filename)[1]}"
        old_file = os.path.join(path, filename)
        new_file = os.path.join(path, new_name)
        # os 模块提供了重命名文件和目录的函数 rename()，如果指定的路径是文件，则重命名文件；反之，如果执行的路径是目录，则重命名目录
        # os.rename(src, dst)
        os.rename(old_file, new_file)

if __name__ == '__main__':
    # 使用示例：
    batch_rename('/path/to/your/directory','file_','.txt')