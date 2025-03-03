#!/usr/local/bin/python3.9

import subprocess

def read_file(file:str) -> str:
    
    command = ['cat', file]
    #command = ['ls', '-a']
    
    try:
        process = subprocess.run(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
        #process = subprocess.Popen(command, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    except FileNotFoundError:
        print("File not found")

    print(process)
    print(process.stdout)
    print(process.stderr)

read_file("./data.txt")
