s='HelloPython,HelloJava,hellophp'
word=input('请输入要统计的字符:')
print('{0}在{1}一共出现了{2}'.format(word,s,s.upper().count(word)))