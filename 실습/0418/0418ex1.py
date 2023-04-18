'''
2023.04.18
김영빈
첫번째
'''

num = int(input('성적 입력 :'))

if num >= 70:
    if num >= 80:
        if num >=90:
            print('A')
        else:
            print('B')
    else:
        print('C')
else:
    print('F')

