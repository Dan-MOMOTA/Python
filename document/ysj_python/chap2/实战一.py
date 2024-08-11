fp=open('text.txt','w') # 打开文件
print('人生苦短，我用Python',file=fp) # 输出内容到文件
fp.close() # 关闭文件