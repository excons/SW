'''
2023.05.09
김영빈
#문제정의
    두 개의 숫자를 입력 받아서 두 수 사이의 합계 구하기
#문제분석
    변수
        num1(정수1),num2(정수2),sum(합계),temp(저장)
    수식
        sum=sum+num1
#알고리즘
    1.변수선언(변수 초기화)
        num1,num2 정수입력받기
        sum=0
    2.프로그램 논리(선택,반복)
        2-1(선택) 항상 num1 > num2
        if num1 > num2:
            temp = num1
            num1 = num2
            num2 = temp
        2-2(반복) num1~num2까지 1씩 증가하면서 더하기
            while num1<=num2:
                sum = sum + num1
                num1+=1
'''

num1 = int(input('첫 번째 숫자 입력 :'))
num2 = int(input('두 번째 숫자 입력 :'))

if num1 > num2:

    temp = num1
    num1 = num2
    num2 = temp

print(num1,'부터',num2,'까지의 합은 :',end='')
sum=0

while num1<=num2:
    sum = sum + num1
    num1+=1

print(sum)