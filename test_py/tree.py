#*************************** Copyright (c) ****************************
# @file    :   tree.py
# @author  :   Dan
# @date    :   2024-05-18
# @version :   V1.0
# @brief   :   

def print_tree(length):
    for i in range(1,length+1):
        print(" "*(length-i)+("*-"*i).strip("-"))
    for i in range(0,length//2):
        print(" "*(length-2)+"|"+" "+"|")

print_tree(16)

