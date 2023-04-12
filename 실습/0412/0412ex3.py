'''
2023.04.12
김영빈
세번째
'''

num1 = int(input('첫 번째 숫자 입력 :'))
num2 = int(input('두 번째 숫자 입력 :'))

if num1%2 == 0 and num2%2 == 0:
    print('두 숫자가 모두 짝수 입니다.')
elif num1%2 ==1 and num2%2 == 1:
    print('두 숫자가 모두 홀수 입니다.')
else :
    print('짝수와 홀수가 섞여 있습니다.')