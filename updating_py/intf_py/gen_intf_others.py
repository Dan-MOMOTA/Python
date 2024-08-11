#*************************** Copyright (c) ****************************
# @file    :   gen_intf.py
# @author  :   Dan
# @date    :   2024-05-29
# @version :   V1.0
# @brief   :   抓取设计文件顶层端口信息并生成interface的小脚本

import os
import sys
import re

#Kang_chengqian_common_python.py在底下路径
#sys.path.append("/home/Kang chengqian/My_script")
#from Kang_chengqian_common_python import *

def shellcmd(cmd):
    print('Now execute shell cmd :'+cmd)
    file_content = os.popen(cmd).read()
    return file_content
def echo(Author):
    print("The script:"+sys.argv[0]+" is written by "+Author)

class ModuleParse():
    def __init__(self):
        self.modulePort = dict()
        self.filePath   = ""

    def inputFilePath(self,path):
        self.filePath = path

    def portParse(self):
        #*?:问号表示非贪婪匹配
        #re.DOTALL表示跨行匹配
        design_head = re.findall(r'module\s+\w+\s*\(.*?\);',shellcmd("cat "+self.filePath),re.DOTALL)
        #print(design_head)
        if(re.findall(r'(input|output)',design_head[0].strip())):
            #以\n切片
            for i in design_head[0].strip().split("\n"):
                if(re.findall(r"(input|output)\s*(wire|reg)\s*(\[[0-9]+\s*\:\s*[0-9]+\])*\s*(\w+)",i)):
                #if(re.findall(r"(input|output)\s*(\[[0-9]+\s*\:\s*[0-9]+\])*\s*(\w+)",i)):
                    signalDirect    = re.findall(r"(input|output)\s*(wire|reg)\s*(\[[0-9]+\s*\:\s*[0-9]+\])*\s*(\w+)",i)[0][0]
                    signalType      = re.findall(r"(input|output)\s*(wire|reg)\s*(\[[0-9]+\s*\:\s*[0-9]+\])*\s*(\w+)",i)[0][1]
                    signalWidthStr  = re.findall(r"(input|output)\s*(wire|reg)\s*(\[[0-9]+\s*\:\s*[0-9]+\])*\s*(\w+)",i)[0][2]
                    signalName      = re.findall(r"(input|output)\s*(wire|reg)\s*(\[[0-9]+\s*\:\s*[θ-9]+\])*\s*(\w+)",i)[0][3]
        else:
            for i in re.findall (r"(input|output)\s*(wire|reg)*\s*(\[[0-9]+\])*\s*(\w+)",shellcmd("cat "+self.filePath)):
                signalDirect    = i[0]
                signalType      = i[1]
                signalWidthStr  = i[2]
                signalName      = i[3]
        if(signalWidthStr):
            temp = re.findall(r"\[([0-9]+)\s*\:\s*([0-9]+)\]",signalWidthStr)[0]
            signalWidth = int(temp[0])-int(temp[1])+1
        else:
            signalWidth =1
        self.modulePort[signalName] = [signalDirect,signalType,signalWidth]

class GensystemVerilogInterface:
    def __init__(self):
        self.ifName     = ""
        self.ifPort     = dict()
        self.ifFilePath = ""

    def input_argv(self,name,port):
        self.ifName = name
        self.ifPort = port
    
    def output_argv(self,ifFilePath):
        self.ifFilePath = ifFilePath
    
    def gen_if(self):
        with open(self.ifFilePath,"w") as fileHandle:
            fileHandle.write("interface "+self.ifName+" ();\n")
            for interface_port in self.ifPort.keys():
                fileHandle.write("logic ["+str(self.ifPort[2]-1)+':0]'+'\t'+interface_port+"\t; \n")
            fileHandle.write("endinterface")

if __name__ == "__main__":
    echo("Dan")
    moduleParse = ModuleParse()
    moduleParse.inputFilePath("./top.v")
    moduleParse.portParse()
    genif = GensystemVerilogInterface()
    genif.input_argv("demo_interface",moduleParse.modulePort)
    genif.output_argv("./demo_interface.sv")
    genif.gen_if()