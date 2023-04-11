'''
2023.04.11
김영빈
두번째
'''

score = int(input('성적을 입력하시오 :'))

if score >= 90:
    print('A')
elif 90>score>=80:
    print('B')
elif 80>score>=70:
    print('C')
else:print('F')