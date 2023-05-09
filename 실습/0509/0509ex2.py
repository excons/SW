'''
2023.05.09
김영빈
#문제정의
    1~1000까지의 숫자 중에 입력받은 숫자의 배수만 더하기
#문제분석
    변수
    num(정수),sum(합계)
#알고리즘
    1.변수초기화
        sum=0
    2.프로그램 논리(for반복)
        for i in range(num, 1001, num):
            sum+=i
'''

num = int(input('합을 원하는 배수 입력 :'))

sum = 0#변수 초기화

for i in range(num, 1001, num):#반복조건
    sum+=i#증감식

print('1부터 1000까지의 {}의 배수의 합은 :{}'.format(num,sum))