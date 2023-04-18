'''
2023.04.18
김영빈
세번째
144쪽 05번
'''

num1 = int(input('첫 번째 정수를입력하세요 :'))
num2 = int(input('두 번째 정수를입력하세요 :'))

if num1 % num2 == 0:
    print(num2,'는',num1,'의 약수 입니다.')
else:
    print(num2,'는',num1,'의 약수가 아닙니다.')