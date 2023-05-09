'''
2023.05.05
김영빈
#문제정의
    입력받은 정수의 팩토리얼 값을 구하라
#문제분석
    1.변수
    num(정수입력),fac(팩토리얼값)
    2.수식
    fac=fac*i
#알고리즘
    1.변수선언
        num 정수입력받기
        fac=1 변수초기화
    2.프로그램 논리(반복)
        for i in range(num,0,-1)
'''

num = int(input('팩토리얼 숫자 입력 :'))

fac=1#곱할거기때문에 1로 초기화

for i in range(num,0,-1):
    fac = fac*i

print('%d 의 팩토리얼 값은 :'%num,fac)