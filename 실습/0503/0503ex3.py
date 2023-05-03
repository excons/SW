'''
2023.05.03
김영빈
반복문 1~입력받은 숫자까지의 합게 구하기
#문제분석
    변수-숫자(num), 합(sum)
#알고리즘
    1.변수선언
        num에 정수 입력받기
        sum 초기화
    2.논리(반복)
        (조건)for i in range(1, num+1):
            sum+=1
        (조건)while i<=num:
            sum+=i
            i+=1
'''

num = int(input('숫자 입력 :'))

#for
sum=0
for i in range(1, num+1):
    sum+=i
print('1~{}까지의 합은 : {}'.format(num,sum))

#while
i=0
sum = 0
while i<=num:
    sum+=i
    i+=1
print('1~{}까지의 합은 : {}'.format(num,sum))