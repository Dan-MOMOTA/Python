import re
pattern='黑客|破解|反爬'
s='我想学习Python，想破解一些VIP视频，Python可以实现无底线反爬吗？'
new_s=re.sub(pattern,'XXX',s)
print(new_s)

s2='https://www.baidu.com/s?wd=ysj&rsv_spt=1'
pattern2='[?|&]'
lst=re.split(pattern2,s2)
print(lst)

