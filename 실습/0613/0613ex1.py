'''
2023.06.13
김영빈
문제정의
    3개의 매개변수를 전달 받아서 가장 큰 값을 리턴하는
    findmax(a,b,c)함수 구현
알고리즘
    1.findmax(a,b,c)함수 선언
        1.1 a,b,c중 가장 큰 값 찾기
    2.a,b,c 입력받기
    3.findmax함수 호출해서 입력받은값 넣기
    4.출력
'''

def findmax(a,b,c):
    if a>b:
        bignum = a
    else:
        bignum = b
    if bignum < c:
        bignum = c
    
    return bignum

a = int(input('첫 번째 숫자 입력 :'))
b = int(input('두 번째 숫자 입력 :'))
c = int(input('세 번째 숫자 입력 :'))

biggistnum = findmax(a,b,c)
print('가장 큰 수는 :',biggistnum)