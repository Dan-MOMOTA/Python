import pandas as pd
import re
import os
import time

#调用anohter.py脚本完成两个excel表格的校验
os.system('anohter.py')
check = os.popen('anohter.py','r') # 启动另一个Python脚本并读取其输出
check_message = check.readlines()
check_message_len = len(check_message)
for i in range(0,check_message_len):
    if(re.search('ERROR',check_message[i])):
        print('check failed')
        quit()
#调用结束，开始读excel
        
file_name = ''
file_time = ''
cur_path = os.path.realpath(__file__)
up_up_dir = os.path.dirname(os.path.dirname(cur_path))
#print(up_up_file)
sub_files = [x[2] for x in os.walk(up_up_dir)]
for sub_file in sub_files:
    if 'python' in sub_file:
        continue
    for item in sub_file:
        if(re.search('SFR_TRIM',item)):
            continue
        ft = time.ctime(os.path.getmtime('../'+item))
        file_name = item
print(file_name)

sfr_path_list = []
sfr_condition_list = []
sfr_ignore_list = []
#特殊功能的信号，需要额外处理
restart_list = ['sfr_reset'] #重启的信号
sleep_list = ['sleep']
tgth_en = [] #联动的使能信号
tgth_cdt = [] #计数器变动的条件
tgth_cnt = [] #计数器本体

##### SFR表格对应的全局变量声明 #####
reg_address_list = [] #寄存器组地址
mark_list = [] #标记寄存器组内第一个寄存器
path_list = [] #标记寄存器组内第一个寄存器
condition_list = [] #标记寄存器组内第一个寄存器
ignore_list = [] #标记寄存器组内第一个寄存器
reserve_list = [] #reserve寄存器标志
address_list = [] #各个寄存器对应的地址
special_list = [] #组内的寄存器是否为特殊寄存器
name_list = [] #寄存器名称
bits_list = [] #寄存器所属bit位置，示例:7:4
access_list = [] #寄存器可操作类型，示例:RW RO
reset_list = [] # 寄存器复位值，示例:8'b0
option_list = [] #寄存器option使能，比如otp写使能
option_address_list = [] #寄存器option地址
option_bits_list = [] #寄存器option所属bit位置
out_bits_list = [] #寄存器输出位宽，由所属bit位置计算而来，示例:3:0
out_bits_min_list = [] 
out_bits_max_list= []
out_width_list = [] #寄存器位宽，由所属bit位置计算而来，示例:4
name_align_list = [] #经过对齐之后的寄存器名称，统一对齐为20个字符
start_bit = []

in_reg_address_list = []
in_mark_list = []
in_path_list = []
in_condition_list = []
in_ignore_list = []
in_reserve_list = []
in_address_list = []
in_special_list = []
in_name_list = []
in_bits_list = []
in_access_list = []
in_reset_list = []
in_option_list = []
in_option_address_list = []
in_option_bits_list = []
in_out_bits_list = []
in_out_bits_min_list = []
in_out_bits_max_list= []
in_out_width_list = []
in_name_align_list = []
in_start_bit = []

address_list_range = range(0,0) #寄存器个数范围
address_list_index_max = 0 #寄存器个数最大值
reg_address_list_range = range(0,0) #寄存器组组数范围
reg_address_list_index_max = 0 #寄存器组组数最大值

##### Trim表格对应的全局变量声明 #####
mt_addr_dir = {} #Trim寄存器地址
mt_name_dir = {} #Trim寄存器名称
mt_reset_dir = {} # Trim寄存器名称

mt_excel_list_len = 0 #Trim excel有效列数
mt_excel_list_index_max = 0 #Trim excel有效列数最大值
mt_excel_list_range = range(0,0) #Trim excel有效列数范围

##### 子函数：读取并解析Trim excel表格 #####
#从Trim Excel表格中，通过寄存器名称来读取寄存器的option地址
def mt_read_excel_file():
    #声明excel文件名称和读取的子sheet名称和需要读取的列数，需要根据不同的项目进行修改
    mt_excel = pd.read_excel('../'+file_name,sheet_name='TRIM',usecols=[0,1,2,3],names=None,keep_default_na=False)
    print(mt_excel)
    MT_EXCEL_ADDR_COL = 0 #Trim表格中，地址所在列数，需要根据不同项目进行修改
    MT_EXCEL_NAME_COL = 1 #Trim表格中，名称所在列数，需要根据不同项目进行修改
    MT_EXCEL_RESET_COL = 3 #Trim表格中，复位值所在列数，需要根据不同项目进行修改

    mt_excel_list = mt_excel.values.tolist()
    print(mt_excel_list)

    global mt_excel_list_len
    global mt_excel_list_index_max
    global mt_excel_list_range

    mt_excel_list_len = len(mt_excel_list)
    mt_excel_list_index_max = mt_excel_list_len - 1
    mt_excel_list_range = (0,mt_excel_list_len)

    global mt_addr_dir
    global mt_name_dir
    global mt_reset_dir

    for i in mt_excel_list_range:
        mt_addr_dir[i] = mt_excel_list[i][MT_EXCEL_ADDR_COL]
        #将寄存器名称全部转换为小写字母
        mt_name_dir[i] = str(mt_excel_list[i][MT_EXCEL_NAME_COL]).lower()
        mt_reset_dir[i] = mt_excel_list[i][MT_EXCEL_RESET_COL]

##### 子函数：读取excel列表 #####
def sfr_read_excel_file():
    excel = pd.read_excel('../'+file_name,sheet_name='EXSFR',usecols=[0,1,2,3,4,5],names=None,keep_default_na=False)
    
    excel_list = excel.values.tolist()
    print(excel_list)
    excel_list_len = len(excel_list)
    print(excel_list_len)
    excel_list_index_max = excel_list_len - 1
    excel_list_range = range(0,excel_list_len)

    global reg_address_list
    global mark_list
    global path_list
    global reserve_list
    global address_list
    global special_list
    global name_list
    global bits_list
    global access_list
    global reset_list
    global option_list
    global option_address_list
    global option_bits_list
    global out_bits_list
    global out_bits_min_list
    global out_bits_max_list
    global out_width_list
    global name_align_list
    global start_bit

    EXCEL_NAME_COL = 0 #Trim表格中，名称所在列数，需要根据不同项目进行修改
    EXCEL_BITS_COL = 1 #Trim表格中，Bits所在列数，需要根据不同项目进行修改
    EXCEL_ACCRESS_COL = 2 #Trim表格中，Access域所在列数，需要根据不同项目进行修改
    EXCEL_RESET_COL = 3 #Trim表格中，Reset域所在列数，需要根据不同项目进行修改
    EXCEL_OPTION_COL = 4 #Trim表格中，Option域所在列数，需要根据不同项目进行修改
    EXCEL_EXSFR_WE_COL = 5 #Trim表格中，exsfr write en域所在列数，需要根据不同项目进行修改

    address = ''
    special = ''
    mark = ''
    bits = ''
    option_address_match = ''
    path = ''

    mt_match_name = ''
    mt_match_option_address = ''

    for i in excel_list_range:
        #print(excel_list[i])
        if(pd.isna((excel_list[i][0]) == 1)):
           #print("empty line detected")
           continue
        #获取地址，暂存下来
        elif(re.match('^[O][a-z]+',excel_list[i][0])):
            address = re.search('^[0][x](\w+)',excel_list[i][1]).group(1).lower()
            reg_address_list.append(address)
            mark = '1'
        #获取special标志，暂存下来
        elif(re.match('^[S][a-z]+',excel_list[i][0])):
            special = excel_list[i][1]
        #获取寄存器信息
        elif(re.match('^[a-z]+',excel_list[i][0])):
            #reserve标志
            if(excel_list[i][0] == 'reversed'):
                reserve_list.append('1')
            else:
                reserve_list.append('0')
            #其他信息
            mark_list.append(mark)
            mark = '0'
            address_list.append(address)
            special_list.append(special)
            name_list.append(excel_list[i][EXCEL_NAME_COL])
            #将bits域中空格删掉
            bits = str(excel_list[i][EXCEL_BITS_COL]).replace(' ','')
            bits_list.append(bits)
            if(re.search(':',bits)):
                start_bit.append(re.search(':(\d+)',bits).group(1))
            else:
                start_bit.append(bits)
            if(excel_list[i][EXCEL_EXSFR_WE_COL] != ''):
                if(excel_list[i][EXCEL_EXSFR_WE_COL] == 'RW0'):
                    access_list.append('W0C')
                elif(excel_list[i][EXCEL_EXSFR_WE_COL] == 'AC'):
                    access_list.append('RW')
                else:
                    access_list.append(excel_list[i][EXCEL_EXSFR_WE_COL])
            else:
                access_list.append(excel_list[i][EXCEL_EXSFR_WE_COL])
            reset_list.append(str(excel_list[i][EXCEL_RESET_COL]))
            option_list.append(excel_list[i][EXCEL_OPTION_COL])
    #prtin(address_list)
    #pritn(special_list)

    mark_list.append('1')

    global address_list_range
    global address_list_index_max
    #获取address列表长度
    address_list_len = len(address_list)
    address_list_index_max = address_list_len - 1
    address_list_range = rangr(0,address_list_len)

    global reg_address_list_range
    global reg_address_list_index_max
    #获取reg_address列表长度
    reg_address_list_len = len(reg_address_list)
    reg_address_list_index_max = reg_address_list_len - 1
    reg_address_list_range = rangr(0,reg_address_list_len)    

    #计算寄存器位宽
    out_bit_int = 0
    out_width_int = 0
    bits_recom = re.compile(r'(\d+)\:s*(\d+)')
    bits_single_recom = re.compile(r'(\d+)')
    bits_match = ''
    for i in address_list_range:
        bits_match = bits_recom.match(str(bits_list[i]))
        bits_single_match = bits_single_recom.match(str(bits_list[i]))
        #debug打印
        #print(bits_match)
        if(bits_match != None):
            out_bit_int = int(bits_match.group(1)) - int(bits_match.group(2))
            out_bits_min_list.append(int(bits_match.group(2)))
            out_bits_max_list.append(int(bits_match.group(1)))
            out_width_int = out_bit_int + 1
            out_bits_list.append("["+str(out_bit_int)+":0]")
            out_width_list.append(str(out_width_int))
        else:
            out_bits_list.append('    ')
            out_width_list.append('1')
            out_bits_min_list.append(int(bits_single_match.group(1)))
            out_bits_max_list.append(int(bits_single_match.group(1)))
    #print(out_bits_list)
    #通过out_bits_list来获取完整的path.list()

    #从Trim excel表格中，通过寄存器名称来读取寄存器的option地址
    option_address_recom = re.compile(r'^[0][x](\w+)\[((\d+)\:?(\d))\]')
    mt_option_width = 0
    for i in address_list_range:
        if(option_list[i] != 'yes'):
            option_address_list.append('')
            option_bits_list.append('')
        else:
            #从Trim excel表格中，通过寄存器名称来读取寄存器的option地址
            for j in mt_excel_list_range:
                if(name_list[i] == mt_name_dir[j]):
                    mt_match_name = mt_name_dir[j]
                    mt_match_option_address = str(mt_addr_dir[j])
            if(mt_match_name == ''):
                #Trim表中未找到对应的option，报错并退出
                print('[ERROR] cannot find the option register name form Trim excel,option register name is '+name_list[i]+' address is '+address_list[i])
                input('wait to exit')
                quit()
                #debug打印
                mt_match_name = ''
                #print('success find the option register name form Trim excel,option register name is '+name_list[i]+' address is '+address_list[i])
            #将Trim表address域中的空格删掉
            option_address_match = option_address_recom.match(mt_match_option_address.replace(' ',''))
            if(option_address_match.group(4) == ''):
                mt_option_width = 1
            else:
                mt_option_width = int(option_address_match.group(3)) - int(option_address_match.group(4)) + 1
            #位宽匹配时，将option地址和所属bit位置写到对应列表中
            if(mt_option_width == int(out_width_list[i])):
                #debug打印
                #print('match register is '+name_list[i])
                option_address_list.append(option_address_match.group(1))
                option_bits_list.append(option_address_match.group(2))
            #位宽不匹配时，报错并退出
            else:
                print('[ERROR] option register bit mismatch,option register name is '+name_list[i]+' address is '+address_list[i])
                input('wait to exit')
                quit()
    #寄存器名称对齐(统一对齐到20个字符)
    for i in address_list_range:
        name_align_list.append("{:<25s}".format(name_list[i]))            

def sfr_inner_read_excel_file():
    in_excel = pd.read_excel('../'+file_name,sheet_name='SFR',usecols=[0,1,2,3,4,5],names=None,keep_default_na=False)

    in_excel_list = in_excel.values.tolist()
    in_excel_list_len = len(in_excel_list)
    #print(excel_list_len)
    in_excel_list_index_max = in_excel_list_len - 1
    in_excel_list_range = range(0,in_excel_list_len)

    global in_reg_address_list
    global in_mark_list
    global in_path_list
    global in_reserve_list
    global in_address_list
    global in_special_list
    global in_name_list
    global in_bits_list
    global in_access_list
    global in_reset_list
    global in_option_list
    global in_option_address_list
    global in_option_bits_list
    global in_out_bits_list
    global in_out_bits_min_list
    global in_out_bits_max_list
    global in_out_width_list
    global in_name_align_list
    global in_start_bit

    EXCEL_NAME_COL = 0 #Trim表格中，名称所在列数，需要根据不同项目进行修改
    EXCEL_BITS_COL = 1 #Trim表格中，Bits所在列数，需要根据不同项目进行修改
    EXCEL_ACCRESS_COL = 2 #Trim表格中，Access域所在列数，需要根据不同项目进行修改
    EXCEL_RESET_COL = 3 #Trim表格中，Reset域所在列数，需要根据不同项目进行修改
    EXCEL_OPTION_COL = 4 #Trim表格中，Option域所在列数，需要根据不同项目进行修改
    EXCEL_EXSFR_WE_COL = 5 #Trim表格中，exsfr write en域所在列数，需要根据不同项目进行修改

    address = ''
    special = ''
    mark = ''
    bits = ''
    option_address_match = ''
    path = ''

    mt_match_name = ''
    mt_match_option_address = ''

    for i in in_excel_list_range:
        #print(in_excel_list[i])
        if(pd.isna((in_excel_list[i][0]) == 1)): # 检查 in_excel_list 中第i行第一个元素是否为缺失值（NaN）
           #print("empty line detected")
           continue
        #获取地址，暂存下来
        elif(re.match('^[O][a-z]+',in_excel_list[i][0])):
            address = re.search('^[0][x](\w+)',in_excel_list[i][1]).group(1).lower()
            in_reg_address_list.append(address)
            mark = '1'
        #获取special标志，暂存下来
        elif(re.match('^[S][a-z]+',in_excel_list[i][0])):
            special = in_excel_list[i][1]
        #获取寄存器信息
        elif(re.match('^[a-z]+',in_excel_list[i][0])):
            #reserve标志
            if(in_excel_list[i][0] == 'reversed'):
                in_reserve_list.append('1')
            else:
                in_reserve_list.append('0')
            #其他信息
            in_mark_list.append(mark)
            mark = '0'
            in_address_list.append(address)
            in_special_list.append(special)
            in_name_list.append(in_excel_list[i][EXCEL_NAME_COL])
            #将bits域中空格删掉
            bits = str(in_excel_list[i][EXCEL_BITS_COL]).replace(' ','')
            bits_list.append(bits)
            if(re.search(':',bits)):
                start_bit.append(re.search(':(\d+)',bits).group(1))
            else:
                start_bit.append(bits)
            if(in_excel_list[i][EXCEL_EXSFR_WE_COL] != ''):
                if(in_excel_list[i][EXCEL_EXSFR_WE_COL] == 'RW0'):
                    in_access_list.append('W0C')
                elif(in_excel_list[i][EXCEL_EXSFR_WE_COL] == 'AC'):
                    in_access_list.append('RW')
                else:
                    in_access_list.append(in_excel_list[i][EXCEL_EXSFR_WE_COL])
            else:
                in_access_list.append(in_excel_list[i][EXCEL_EXSFR_WE_COL])
            in_reset_list.append(str(in_excel_list[i][EXCEL_RESET_COL]))
            in_option_list.append(in_excel_list[i][EXCEL_OPTION_COL])
    #prtin(in_address_list)
    #pritn(in_special_list)

    in_mark_list.append('1')

    global in_address_list_range
    global in_address_list_index_max
    #获取address列表长度
    in_address_list_len = len(in_address_list)
    in_address_list_index_max = in_address_list_len - 1
    in_address_list_range = rangr(0,in_address_list_len)

    global in_reg_address_list_range
    global in_reg_address_list_index_max
    #获取reg_address列表长度
    in_reg_address_list_len = len(in_reg_address_list)
    in_reg_address_list_index_max = in_reg_address_list_len - 1
    in_reg_address_list_range = rangr(0,in_reg_address_list_len)    

    #计算寄存器位宽
    out_bit_int = 0
    out_width_int = 0
    bits_recom = re.compile(r'(\d+)\:s*(\d+)')
    bits_single_recom = re.compile(r'(\d+)')
    bits_match = ''
    for i in in_address_list_range:
        bits_match = bits_recom.match(str(in_bits_list[i]))
        #bits_single_match = bits_single_recom.match(str(bits_list[i]))
        #debug打印
        #print(bits_match)
        if(bits_match != None):
            out_bit_int = int(bits_match.group(1)) - int(bits_match.group(2))
            out_width_int = out_bit_int + 1
            out_bits_list.append("["+str(out_bit_int)+":0]")
            out_width_list.append(str(out_width_int))
        else:
            out_bits_list.append('    ')
            out_width_list.append('1')

def sfr_uvm_gen():
    sfr_uvm = open('reg_model.sv','w')
    t = time.localtime()
    #define地址
    sfr_uvm.write('// Version \n')
    sfr_uvm.write('// SFR excel name : '+file_name+'\n')
    sfr_uvm.write('// SFR excel time : '+ft+'\n')
    sfr_uvm.write('// Genrate date   : '+str(t.tm_year)+'/'+str(t.tm_mon)+'/'+str(t.tm_mday)+'/'+str(t.tm_hour)+'h/'+str(t.tm_min)+'min/'+str(t.tm_sec)+'s'+'\n')
    sfr_uvm.write('// Function       : for sfr test \n')
    sfr_uvm.write('`ifndef REG_MODEL_SV \n')
    sfr_uvm.write('`define REG_MODEL_SV \n')
    
    sfr_address_all_list = []
    sfr_name_all_list = []
    sfr_bits_all_list = []
    sfr_access_all_list = []
    sfr_reset_all_list = []
    sfr_reserve_all_list = []
    sfr_start_bit_all_list = []
    sfr_address_all_list = in_address_list + address_list
    sfr_name_all_list = in_name_list + name_list
    sfr_out_width_all_list = in_out_width_list + out_width_list
    sfr_access_all_list = in_access_list + access_list
    sfr_reset_all_list = in_reset_list + reset_list
    sfr_reserve_all_list = in_reserve_list + reserve_list
    sfr_start_bit_all_list = in_start_bit + start_bit

    reg_addr = ''
    name_addr = ''
    name_addr_list = []
    for i in range(0,128):
        reg_addr = str(hex(i)).replace('0x','').rjust(2,'0')
        name_addr = 'reg_'+reg_addr
        if(reg_addr in sfr_address_all_list):
            name_addr_list.append(name_addr)
            sfr_uvm.write('class '+name_addr+' extend uvm_reg; \n')
            #sfr_uvm.write('\n)
            for j in range(0,len(sfr_address_all_list)):
                if(sfr_reserve_all_list[j] == reg_addr):
                    if(sfr_reserve_all_list[j] == '1'):
                        continue
                    else:
                        sfr_uvm.write('    rand uvm_reg_field '+sfr_name_all_list[j]+'; \n')
            #sfr_uvm.write('\n)
            sfr_uvm.write('    virtual function void build(); \n')
            for j in range(0,len(sfr_address_all_list)):
                if(sfr_address_all_list[j] == '1'):
                    continue
                else:
                    srf_uvm.write('    '+sfr_name_all_list[j].ljust(20,'')+' = uvm_reg_field::type_id::create("'+sfr_name_all_list[j]+'"); \n')
            sfr_uvm.write('    endfunction \n')
            sfr_uvm.write('    `uvm_object_utils('+name_addr+')\n')
            sfr_uvm.write('    function new(input string name = "'+name_addr+'"); \n')
            sfr_uvm.write('        super.new(name,8,UVM_NO_COVERAGE); \n')
            sfr_uvm.write('    endfunction \n')
            sfr_uvm.write('endclass \n')
            name_addr_blk = name_addr +'_blk'
            name_addr_cp = name_addr +'_cp'
            sfr_uvm.write('class '+name_addr_blk+' extends uvm_reg_block; \n')
            sfr_uvm.write('    rand '+name_addr+' '+name_addr_cp+'; \n')
            sfr_uvm.write('    vitrual function void build(); \n')
            sfr_uvm.write('        defautlt_map = create_map("default_map",0,1,UVM_LITTLE_ENDIAN,0); \n')
            sfr_uvm.write('       '+name_addr_cp+'= '+name_addr+'::type_id::create("'+name_addr_cp+'",,get_full_name); \n')
            sfr_uvm.write('       '+name_addr_cp+'.configure(this,null,""); \n')
            sfr_uvm.write('       '+name_addr_cp'.build(); \n')
            for j in range(0,len(sfr_address_all_list)):
                if(sfr_address_all_list[j] == reg_addr):
                    if(sfr_reserve_all_list[j] == '1'):
                        continue
                    else:
                        sfr_uvm.write('    '+name_addr_cp+'.'+sfr_name_all_list[j]+'.configure('+name_addr_cp+','+sfr_out_width_all_list[j]+','+sfr_start_bit_all_list[j]+','+sfr_access_all_list[j]+'",1,'+sfr_reserve_all_list[j]+',1,1,0); \n')
                        sfr_uvm.write('    '+name_addr_cp+'.add_hdl_path_slice("'+sfr_name_all_list[j]+'",'+sfr_start_bit_all_list[j]+','+sfr_out_width_all_list[j]+'); \n')
            sfr_uvm.write('        default_map.addr_reg('+name_addr_cp+',\'h'+reg_addr+',"RW"); \n')
            sfr_uvm.write('    endfunction \n')
            sfr_uvm.write('    `uvm_object_utils('+name_addr_blk+') \n')
            sfr_uvm.write('    function new(input string name = "'+name_addr_blk+'"); \n')
            sfr_uvm.write('        super.new(name,UVM_NO_COVERAGE); \n')
            sfr_uvm.write('    endfunction; \n')
            sfr_uvm.write('endclass; \n')
    sfr_uvm.write('class reg_model extends uvm_reg_block; \n')
    for i in range(0,len(name_addr_list[i])):
        name_addr = name_addr_list[i]
        name_addr_ins = name_addr + '_ins'
        name_addr_blk = name_addr + '_blk'
        sfr_uvm.write('    rand '+name_addr_blk+' '+name_addr_ins+'; \n')
    sfr_uvm.write('    virtual function void build(); \n')
    sfr_uvm.write('        default_map = create_map("default_map",0,1,UVM_LITTLE_ENDIAN,0); \n') 
    for i in range(0,len(name_addr_list)):
        name_addr = name_addr_list[i]
        name_addr_ins = name_addr + '_ins'
        name_addr_blk = name_addr + '_blk'
        sfr_uvm.write('       '+name_addr_ins' = '+name_addr_blk'::type_id::create("'+name_addr_ins+'"); \n')
        sfr_uvm.write('       '+name_addr_ins'.configure(this,""); \n')
        sfr_uvm.write('       '+name_addr_ins'.build(); \n')
        sfr_uvm.write('       '+name_addr_ins'.lock_model(); \n')
        sfr_uvm.write('        default_map.add_submap('+name_addr_ins+'.defautlt_map,8\'h00); \n')        
    sfr_uvm.write('    endfunction; \n')
    sfr_uvm.write('    `uvm_object_utils(reg_model) \n')        
    sfr_uvm.write('    function new(input string name = "reg_model"); \n')
    sfr_uvm.write('        super.new(name,UVM_NO_COVERAGE); \n')        
    sfr_uvm.write('    endfunction \n')
    sfr_uvm.write('endclass \n')        
    sfr_uvm.write('`endif \n')

##### 主函数 #####
if __name__ == '__main__':
    mt_read_excel_file()
    sfr_read_excel_file()
    sfr_inner_read_excel_file()
    sfr_uvm_gen()
    print("reg_model.sv generate success !!!")