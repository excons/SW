'''
2023.04.11
김영빈
세번째
'''

num1 = int(input('첫번째 숫자 입력 :'))

num2 = int(input('두번째 숫자 입력 :'))

op = input('연산자(+,-,*,/) 입력 :')

if op == '+':
    print(num1 + num2)

elif op == '-':
    print(num1 - num2)

elif op == '*':
    print(num1 * num2)

else:
    print(num1 / num2)