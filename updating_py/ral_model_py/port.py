import pandas as pd
import re
import os
import time

#cur_path = os.path.dirname(__file__) # d:\Dan\3.Python\ral_gen
cur_path = os.path.realpath(__file__) # D:\Dan\3.Python\ral_gen\test.py
up_dir = os.path.dirname(cur_path) # D:\Dan\3.Python\ral_gen
up_up_dir = os.path.dirname(up_dir) # D:\Dan\3.Python
sub_files = [x[2] for x in os.walk(up_dir)]
for sub_file in sub_files:
    for item in sub_file:
        if(re.search('reg.xlsx',item)):
            file_name = item        
            ft = time.ctime(os.path.getmtime(item))
            print(item+': '+ft)
            continue
print('\nEXPECT FILE: '+file_name+'\n')

name_list = []
size_list = []
dir_list = []

def read_port_excel():
    excel = pd.read_excel('./'+file_name,sheet_name='PORT',usecols=[0,1,2],names=None,keep_default_na=False)
    print(excel)    
    excel_list = excel.values.tolist()
    #print(excel_list)
    excel_list_len = len(excel_list)
    #print(excel_list_len)
    excel_list_index_max = excel_list_len - 1
    excel_range = range(1, excel_list_len)

    EXCEL_NAME_COL = 0 #PORT表格中，名称所在列数，需要根据不同项目进行修改
    EXCEL_SIZE_COL = 1 #PORT表格中，size所在列数，需要根据不同项目进行修改
    EXCEL_DIR_COL = 2 #PORT表格中，方向所在列数，需要根据不同项目进行修改

    for i in excel_range:
        #print(excel_list[i])
        #if(pd.isna(excel_list[i][0]) == 1): #检查in_excel_list中第i行第一个元素是否为缺失值NaN
        name_list.append(excel_list[i][EXCEL_NAME_COL])
        size_list.append(excel_list[i][EXCEL_SIZE_COL])
        dir_list.append(excel_list[i][EXCEL_DIR_COL])
    print(name_list)
    print(size_list)
    print(dir_list)

def rtl_gen():
    pass


##### 主函数 #####
if __name__ == '__main__':
    read_port_excel()
    rtl_gen()
    print("port.sv generate success !!!")