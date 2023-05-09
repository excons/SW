'''
2023.05.09
김영빈 
#문제정의
    1부터 100까지의 입력받은 숫자의 배수합을 while과 continue를 사용해서 구하라
#문제분석
    변수
        num(정수),i(조건),sum(합)
    수식
        i%num
        sum+=i
#알고리즘
    1.변수초기화
        i=0
        sum = 0
    2.프로그램 논리(while 반복문)
        while i < 100:
            i+=1
            if (i%num) != 0:
                continue
            sum+=i
'''

num = int(input('배수 숫자 입력 :'))
i=0
sum = 0



while i < 100:
    i+=1
    if (i%num) != 0:
        continue
    sum+=i

print('1부터 100까지 %d의 배수의 합은 :'%num,sum)