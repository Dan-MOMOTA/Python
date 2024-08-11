try:
    score=int(input('请输入分数:'))
    if 0<=score<=100:
        print('分数为:',score)
    else:
        raise Exception('分数不正确')
except Exception as e:
    print(e)
