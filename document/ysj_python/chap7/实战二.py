try:
    a=int(input('请输入第一条边长:'))
    b = int(input('请输入第二条边长:'))
    c = int(input('请输入第三条边长:'))
    if a+b>c and a+c>b and b+c>a:
        print(f'三角形的边长为:{a},{b},{c}')
    else:
        raise  Exception(f'{a},{b},{c},不能构成三角形')
except Exception as e:
    print(e)