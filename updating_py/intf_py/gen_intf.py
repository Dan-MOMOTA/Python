import re
import time
import sys

direction_list  = []
data_type_list  = []
bit_width_list  = []
identifier_list = []

# 读取文件内容
def read_rtl(rtl_name):
    global direction_list
    global data_type_list
    global bit_width_list
    global identifier_list

    with open(rtl_name, 'r') as file:
        verilog_code = file.read()
    # 正则表达式匹配端口
    module_pattern = re.compile(r'module\s+\w+\s*\((.*?)\);', re.DOTALL)
    ports_match = module_pattern.search(verilog_code)
    #print(ports_match)
    if ports_match:
        ports_block = ports_match.group(1)
        #print(ports_block)

        # 正则表达式匹配单个端口
        port_pattern = re.compile(r'(\binput\b|\boutput\b)\s+(wire|reg)?\s*(\[.*?\])?\s+([a-zA-Z_]\w*)', re.DOTALL)

        # 找到所有端口
        ports = port_pattern.findall(ports_block)
        #print(ports)
        for i in range(len(ports)):
            # 端口方向、数据类型、位宽和名称 ---解包
            direction, data_type, bit_width, identifier = ports[i]
            direction_list.append(direction)
            data_type_list.append(data_type)
            bit_width_list.append(bit_width)
            identifier_list.append(identifier)
    else:
        print("No module found in the provided Verilog code.")
        #print("-"*50)

def gen_interface(interface_name):
    intf_file = open(interface_name+'.sv','w')
    t = time.localtime()
    intf_file.write('// ============================================= \n')
    intf_file.write('// File_name      : '+interface_name+'_if.sv \n')
    intf_file.write('// Creater        : Dan \n')
    intf_file.write('// Genrate date   : '+str(t.tm_year)+'/'+str(t.tm_mon)+'/'+str(t.tm_mday)+'/'+str(t.tm_hour)+'h/'+str(t.tm_min)+'min/'+str(t.tm_sec)+'s'+'\n')
    intf_file.write('// Function       : interface \n')
    intf_file.write('// ============================================= \n')
    intf_file.write('`ifndef '+interface_name.upper()+'_INTERFACE_SV \n')
    intf_file.write('`define '+interface_name.upper()+'_INTERFACE_SV \n\n')
    # 生成接口代码
    intf_file.write('interface '+interface_name+'_if();\n\n')
    intf_file.write('    parameter setup_time  = 1; // ns\n')
    intf_file.write('    parameter holdup_time = 1; // ns\n\n')
    #gen_port
    for i in range(len(direction_list)):
        intf_file.write('    logic   '+bit_width_list[i].ljust(10)+identifier_list[i].ljust(20)+'; // '+direction_list[i]+'\n')
    intf_file.write('\n    bit               ast_en = 1\'b1 ;\n')
    #gen drv_ck
    intf_file.write('\n    clocking drv_ck @(posedge clk);\n')
    intf_file.write('        default input #setup_time output #holdup_time;\n')
    for i in range(len(direction_list)):
        if direction_list[i] == 'input':
            intf_file.write('        output  '+identifier_list[i].ljust(20)+';\n')
        elif direction_list[i] == 'output':
            intf_file.write('        input   '+identifier_list[i].ljust(20)+';\n')            
    intf_file.write('    endclocking\n')
    #gen mon_ck
    intf_file.write('\n    clocking mon_ck @(posedge clk);\n')
    intf_file.write('        default input #setup_time output #holdup_time;\n')
    for i in range(len(direction_list)):
        intf_file.write('        input   '+identifier_list[i].ljust(20)+';\n')            
    intf_file.write('    endclocking\n\n')
    intf_file.write('// ---------------- ASSERT ---------------- \\\\\n')
    intf_file.write('    initial begin:assert_control\n')
    intf_file.write('        if(ast_en === 1\'b1) begin\n')
    intf_file.write('            fork\n')
    intf_file.write('                forever begin\n')
    intf_file.write('                    wait(rst === 1);\n')
    intf_file.write('                    $assertoff();\n')
    intf_file.write('                    wait(rst === 0);\n')
    intf_file.write('                    $asserton();\n')
    intf_file.write('                 end\n')
    intf_file.write('             join_none\n')
    intf_file.write('         end\n')
    intf_file.write('         else begin\n')
    intf_file.write('             $assertoff();\n')
    intf_file.write('         end\n')
    intf_file.write('     end\n')
    intf_file.write('endinterface\n\n')
    intf_file.write('`endif')

##### 主函数 #####
if __name__ == '__main__':
    read_rtl('top.v')
    gen_interface('aaa')
    #read_rtl(sys.argv[0])
    #rgen_interface(sys.argv[1])
    print("interface generate success !!!")