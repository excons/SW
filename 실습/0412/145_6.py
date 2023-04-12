'''
2023.04.12
김영빈
145쪽6번
'''

num1 = int(input('첫 번째 정수를 입력하세요 :'))

num2 = int(input('두 번째 정수를 입력하세요 :'))

if num1%2 ==0 and num2%2==0:
    print(num1,"+",num2,"=",num1+num2)
elif num1%2 == 1 and num2%2 == 1:
    print('두 숫자 모두 짝수로 입력하세요.')
elif num1%2==1:
    print('첫 번째 정수를 짝수로 입력하세요.')
else:
    print('두 번째 정수를 짝수로 입력하세요.')
