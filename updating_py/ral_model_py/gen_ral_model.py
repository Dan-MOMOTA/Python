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

reg_name_list = []
reg_address_list = []
reg_field_address_list = []
reg_spcial_list = []
reg_field_list = []
reg_bits_list = []
reg_access_list = []
reg_reset_list = []
reg_reserve_list = []
reg_option_list = []
reg_sfr_access_list = []
reg_path_list = []
reg_start_bit_list = []
first_field_mark_list = []
out_bits_list = [] #寄存器输出位宽，由所属bit位置计算而来，示例:3:0
out_width_list = [] #寄存器位宽，由所属bit位置计算而来，示例:4
reg_ins_name_list = [] #reg例化的名字


def read_reg_excel():
    reg_excel = pd.read_excel('./'+file_name,sheet_name='REG',usecols=[0,1,2,3,4,5,6],names=None,keep_default_na=False)
    print(reg_excel)    
    reg_excel_list = reg_excel.values.tolist()
    #print(reg_excel_list)
    reg_excel_list_len = len(reg_excel_list)
    #print(reg_excel_list_len)
    reg_excel_list_index_max = reg_excel_list_len - 1
    reg_excel_range = range(0, reg_excel_list_len)

    EXCEL_FIELD_COL = 0 #Trim表格中，名称所在列数，需要根据不同项目进行修改
    EXCEL_BITS_COL = 1 #Trim表格中，Bits所在列数，需要根据不同项目进行修改
    EXCEL_ACCRESS_COL = 2 #Trim表格中，Access域所在列数，需要根据不同项目进行修改
    EXCEL_RESET_COL = 3 #Trim表格中，Reset域所在列数，需要根据不同项目进行修改
    EXCEL_OPTION_COL = 4 #Trim表格中，Option域所在列数，需要根据不同项目进行修改
    EXCEL_SFR_ACCESS_COL = 5 #Trim表格中，sfr access域所在列数，需要根据不同项目进行修改
    EXCEL_PATH_COL = 6 #Trim表格中，path域所在列数，需要根据不同项目进行修改

    for i in reg_excel_range:
        #print(reg_excel_list[i])
        #if(pd.isna(reg_excel_list[i][0]) == 1): #检查in_excel_list中第i行第一个元素是否为缺失值NaN
        if(reg_excel_list[i][0] == ''):
            #print('EMPTY LINE')
            continue
        # get reg_name
        elif(re.match('^[N][a-z]+',reg_excel_list[i][0])):
            reg_name = reg_excel_list[i][1].lower()
            reg_name_list.append(reg_name)
            #print(reg_name)
        # get address
        elif(re.match('^[O][a-z]+',reg_excel_list[i][0])):
            address = re.search('^[0][x](\w+)',reg_excel_list[i][1]).group(1).lower()
            reg_address_list.append(address)
            mark = '1'
            #print(address)
        # get special
        elif(re.match('^[S][a-z]+',reg_excel_list[i][0])):
            special = reg_excel_list[i][1]
            reg_spcial_list.append(special)
        # get reg information
        elif(re.match('^[a-z]+',reg_excel_list[i][0])):
            #reserve flag
            if(reg_excel_list[i][0] == 'reserved'):
                reg_reserve_list.append('1')
            else:
                reg_reserve_list.append('0')
            #other information
            first_field_mark_list.append(mark)
            mark = '0'
            reg_field_address_list.append(address)
            reg_field_list.append(reg_excel_list[i][EXCEL_FIELD_COL])
            reg_path_list.append(reg_excel_list[i][EXCEL_FIELD_COL])
            #print(reg_excel_list[i][EXCEL_FIELD_COL])
            #将bits域中空格删掉
            #bits = str(in_excel_list[i][EXCEL_BITS_COL]).replace(' ','')
            bits = str(reg_excel_list[i][EXCEL_BITS_COL])
            reg_bits_list.append(bits)
            #print(bits)
            if(re.search(':',bits)):
                reg_start_bit_list.append(re.search(':(\d+)',bits).group(1))
            else:
                reg_start_bit_list.append(bits)
            if(reg_excel_list[i][EXCEL_SFR_ACCESS_COL] != ''):
                if(reg_excel_list[i][EXCEL_SFR_ACCESS_COL] == 'RW0'):
                    reg_access_list.append('W0C')
                elif(reg_excel_list[i][EXCEL_SFR_ACCESS_COL] == 'AC'):
                    reg_access_list.append('RW')
                elif(reg_excel_list[i][EXCEL_SFR_ACCESS_COL] == 'RW_NO'):
                    reg_access_list.append('RW')   
                else:
                    reg_access_list.append(reg_excel_list[i][EXCEL_ACCRESS_COL])
            else:                
                reg_access_list.append(reg_excel_list[i][EXCEL_ACCRESS_COL])
            reg_reset_list.append(reg_excel_list[i][EXCEL_RESET_COL])
            reg_option_list.append(reg_excel_list[i][EXCEL_OPTION_COL])
    #first_field_mark_list.append('1')
    print('reg_name_list:\n'+str(reg_name_list))
    print('reg_address_list:\n'+str(reg_address_list))
    print('reg_field_address_list:\n'+str(reg_field_address_list))
    print('reg_spcial_list:\n'+str(reg_spcial_list))
    print('reg_field_list:\n'+str(reg_field_list))
    print('reg_bits_list:\n'+str(reg_bits_list))
    print('reg_access_list:\n'+str(reg_access_list))
    print('reg_reset_list:\n'+str(reg_reset_list))
    print('reg_reserve_list:\n'+str(reg_reserve_list))
    print('reg_option_list:\n'+str(reg_option_list))
    print('reg_path_list:\n'+str(reg_path_list))
    print('reg_start_bit_list:\n'+str(reg_start_bit_list))
    print('first_field_mark_list:\n'+str(first_field_mark_list))

    #计算多少个寄存器
    global reg_address_list_range
    global reg_address_list_index_max
    address_address_list_len = len(reg_address_list)
    reg_address_list_range = range(0,address_address_list_len)
    reg_address_list_index_max = address_address_list_len - 1

    #计算多少个域
    global reg_field_address_list_range
    global reg_field_address_list_index_max
    reg_field_address_list_len = len(reg_field_address_list)
    reg_field_address_list_range = range(0,reg_field_address_list_len)
    reg_field_address_list_index_max = reg_field_address_list_len - 1

    #计算寄存器位宽
    out_bit_int = 0
    out_width_int = 0
    bits_recom = re.compile(r'(\d+)\:s*(\d+)')
    bits_single_recom = re.compile(r'(\d+)')
    bits_match = ''
    for i in reg_field_address_list_range:
        bits_match = bits_recom.match(str(reg_bits_list[i]))
        bits_single_match = bits_single_recom.match(str(reg_bits_list[i]))
        #debug打印
        #print(bits_match)
        if(bits_match != None):
            out_bit_int = int(bits_match.group(1)) - int(bits_match.group(2))
            out_width_int = out_bit_int + 1
            out_bits_list.append("["+str(out_bit_int)+":0]")
            out_width_list.append(str(out_width_int))
        else:
            out_bits_list.append(' ')
            out_width_list.append('1')
    print('out_bits_list:\n'+str(out_bits_list))
    print('out_width_list:\n'+str(out_width_list))

def reg_model_gen():
    global reg_name_list_len
    global reg_name_list_range
    reg_name_list_len = len(reg_name_list)
    reg_name_list_range = range(0,reg_name_list_len)

    reg_uvm = open('reg_model.sv','w')
    t = time.localtime()

    reg_uvm.write('// Version \n')
    reg_uvm.write('// SFR excel name : '+file_name+'\n')
    reg_uvm.write('// SFR excel time : '+ft+'\n')
    reg_uvm.write('// Genrate date   : '+str(t.tm_year)+'/'+str(t.tm_mon)+'/'+str(t.tm_mday)+'/'+str(t.tm_hour)+'h/'+str(t.tm_min)+'min/'+str(t.tm_sec)+'s'+'\n')
    reg_uvm.write('// Function       : for sfr test \n')
    reg_uvm.write('// Creator        : Dan \n \n')
    reg_uvm.write('`ifndef REG_MODEL_SV \n')
    reg_uvm.write('`define REG_MODEL_SV \n')

    for i in reg_address_list_range:
        #reg_addr = str(hex(i)).replace('0x','').rjust(2,'0') #将整数i转换为十六进制表示，并去除前缀'0x'，然后将结果右对齐，不足两位的地方用 '0' 填充
        #reg_name_ = 'trim_'+reg_addr
        reg_name = str(reg_name_list[i])
        reg_uvm.write('class '+reg_name+' extends uvm_reg;\n')
        #field_match = re.search('trim_(\d+)',reg_name_list[i]).group(1)
        field_match = reg_address_list[i]
        #print(field_match)
        for j in reg_field_address_list_range:
            if(field_match in reg_field_address_list[j]):
                if(reg_reserve_list[j] == '1'):
                    continue
                else:
                    reg_uvm.write('\trand uvm_reg_field '+reg_field_list[j]+';\n')
        reg_uvm.write('\n\t`uvm_object_utils('+reg_name+')\n')
        reg_uvm.write('\n\tfunction new(string name = "'+reg_name+'");\n')
        reg_uvm.write('\t\tsuper.new(name, 32, build_coverage(UVM_NO_COVERAGE));\n')
        reg_uvm.write('\tendfunction:new\n')
        reg_uvm.write('\n\tvirtual function void build();\n')
        for j in reg_field_address_list_range:
            if(field_match in reg_field_address_list[j]):
                if(reg_reserve_list[j] == '1'):
                    continue
                else:
                    reg_uvm.write('\t\tthis.'+reg_field_list[j]+' = uvm_reg_field::type_id::create("'+reg_field_list[j]+'", ,get_full_name());\n')      
                    # configure(parent,size,lsb_pos,access,volatile,reset_value,has_reset,is_rand,field);
                    reg_uvm.write('\t\tthis.'+reg_field_list[j]+'.configure(this,'+out_width_list[j]+','+reg_start_bit_list[j]+',"'+reg_access_list[j]+'",1,'+reg_reset_list[j]+',1,1,0);\n')
                    reg_uvm.write('\t\tthis.add_hdl_path_slice(.name("'+reg_field_list[j]+'"),.offset('+reg_start_bit_list[j]+'),.size('+out_width_list[j]+'));\n')
                    reg_uvm.write('\n') 
        
        reg_uvm.write('\tendfunction:build\n') 
        reg_uvm.write('endclass:'+reg_name+'\n\n')

    reg_uvm.write('class reg_model extends uvm_reg_block;\n')
    for i in reg_name_list_range:
        reg_uvm.write('\t rand '+reg_name_list[i]+' '+reg_name_list[i]+'_ins;\n')
        reg_ins_name_list.append(str(reg_name_list[i])+'_ins')
    reg_uvm.write('\n\tvirtual function void build();\n')
    # default_map = create_map(name,基地址,总线位宽，以byte为单位,大小端,是否可按byte寻址);
    reg_uvm.write('\t\tdefault_map = create_map("default_map",0,4,UVM_LITTLE_ENDIAN,0);\n\n')
    for i in reg_name_list_range:
        reg_uvm.write('\t\t'+reg_ins_name_list[i]+' = '+reg_name_list[i]+'::type_id::create("'+reg_ins_name_list[i]+'", ,get_full_name());\n')
        reg_uvm.write('\t\t'+reg_ins_name_list[i]+'.configure(this,null,"");\n')
        reg_uvm.write('\t\t'+reg_ins_name_list[i]+'.build();\n')
        reg_uvm.write('\t\tdefault_map.add_reg('+reg_ins_name_list[i]+",'h"+reg_address_list[i]+',"RW");\n\n')
    reg_uvm.write('\tendfunction\n\n')
    reg_uvm.write('\t`uvm_object_utils(reg_model)\n\n')
    reg_uvm.write('\tfunction new(input string name = "reg_moedl");\n')
    reg_uvm.write('\t\tsuper.new(name,UVM_NO_COVERAGE);\n')
    reg_uvm.write('\tendfunction\n\n')
    reg_uvm.write('endclass\n')
    reg_uvm.write('`endif')

##### 主函数 #####
if __name__ == '__main__':
    read_reg_excel()
    reg_model_gen()
    print("reg_model.sv generate success !!!")
