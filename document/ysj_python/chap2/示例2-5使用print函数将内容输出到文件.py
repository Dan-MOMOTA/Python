fp=open('note.txt','w') # 打开文件 w-->write
print('北京欢迎你',file=fp) # 将"北京欢迎你" 输出(写入)到note.txt文件中
fp.close() # 关闭文件
