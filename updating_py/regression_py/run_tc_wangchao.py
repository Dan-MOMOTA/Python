#!/home/path/python3
import re
import os
import sys
import time
import subprocess
#from psutil import *
from time import sleep

sys_list = [] 
tc_path_list = [] 
tc_name_list = [] 
tc_f = '' 
tc_type = '' 
tc_thread = 4 
tc_num = 0 
tc_p = ''

def get_argv():
    global sys_list
    global tc_path_list
    global tc_name_list
    global tc_f 
    global tc_p
    global tc_type 
    global tc_thread
    global tc_num

    path_set = ''
    tc_name = ''
    argv_list = sys.argv
    for i in range(0,len(argv_list)):
        #print(argv_list[i])
        if sys.argv[i] =='-max_thread':
            tc_thread = int(sys.argv[i+1])
        if sys.argv[i] == '-l':
            print(argv_list[i+1])
            path_set = argv_list[i+1]
        if sys.argv[i] == '-f':
            tc_f = ' -f'
        if sys.argv[i] == '-p':
            tc_f = ' -p'
        if sys.argv[i] == '-ff':
            tc_f = ' -ff'
        if sys.argv[i] == '-ss':
            tc_f = ' -ss'
        if sys.argv[i] == '-tt':
            tc_f = ' -tt'  

    #print('[LOG] paht_tc is '+path_tc_list)
    path_tc = open(path_set, 'r')
    path_line = path_tc.readline()
    for line in path_line:
        line = line.strip()
        line = line.replace('./', '')
        tc_path_list.append(line)
        tc_name = line.replace('./', '_').replace('pattern', '').strip('_')
        tc_name_list.append(tc_name)
    tc_num = len(tc_name_list)

def sim_muti():
    tc_name = ''
    runing_thread = 0
    runing_finish = 0
    runing_tc_name = []
    runing_finish_list = []
    while(runing_finish != tc_num):
        runing_finish_list = []
        #print(runing_thread,tc_thread)
        while(runing_thread != tc_thread and runing_finish != tc_num):
        #while(runing_thread != tc_thread and runing_finish != tc_num and cpu_precent(interval=2) < 80):
            tc_path = tc_path_list[runing_finish]
            cmd = 'run'+tc_path+tc_f+tc_p+tc_type
            #print(cmd)
            print('[Simulation] command is: '+cmd)
            subprocess.Popen('gnome-terminal -e \'csh -c \"'+cmd+'\"\'',shell=True)
            #os.system(cmd)
            if tc_p == '':
                tc_name = tc_name_list[runing_finish]
            else:
                tc_name = tc_name_list[runing_finish]+'_post'
            cmd = 'rm '+'log/'+tc_name+'.log'
            os.system(cmd)
            sleep(10)
            com_result = ''
            while(com_result == ''):
                name_com = ''
                if tc_p == '':
                    name_com = 'compile_log'
                else:
                    name_com = 'compile_post.log'
                com = open(name_com, 'r')
                com_read = com.read()
                if 'Error-' in com_read:
                    print('[ERROR] Complie wrong, tc is '+tc_path)
                    com_result = '1'
                if 'simv up to date' in com_read:
                    running_thread = runing_thread + 1
                    running_finish = runing_finish + 1
                    com_result = '1'
                    runing_tc_name.append(tc_name)
            sleep(30)
        #sleep(60)
        #print(runing_tc_name)
        for i in range(0,len(runing_tc_name)):
            name_log = ''
            name_log = 'log/'+runing_tc_name[i]+'.log'
            #print(name_log)
            tc_result = open(name_log, 'r')
            tc_result_read = tc_result.read()
            #runing_thread = running_thread - 1
            #runing_finish_list.append(runing_tc_name[i])
            if 'AM6007_PASS' in tc_result_read:
                print('[Result] '+runing_tc_name[i]+' PASSED !!!')
                runing_thread = running_thread - 1
                runing_finish_list.append(runing_tc_name[i])
            if 'AM6007_FAIL' in tc_result_read:
                print('[Result] '+runing_tc_name[i]+' FAILED !!!')
                runing_thread = running_thread - 1
                runing_finish_list.append(runing_tc_name[i])
            tc_result.close()
        for item in runing_finish_list:
            runing_tc_name.remove(item)

if __name__ == '__main__':
    get_argv()
    sim_muti()
    print('[Log] All tc had been run ...')