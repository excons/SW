'''
2023.06.07
김영빈
문제정의
    랜덤으로 2개의 set 만든 후 합집합, 교집합, 차집합 구하기
문제분석
    변수-num1,num2
알고리즘
    1.랜덤모듈 추가
    2.비어있는 세트 변수 생성
    3.반복(while True)
        3-1.조건문
            num1,num2 가 10개가 댈때까지 반복
            num1=랜덤수 추가
            num2=랜덤수 추가
        3-2.조건문
            num1,num2 가 10개가 될 경우 반복문 종료(break)
    4.합집합, 교집합, 차집합 계산(num1|num2,num1&num2,num1-num2)
    5.출력
'''

import random

num1 = set()
num2 = set()

while True:
    if len(num1) < 10:
        num1.add(random.randint(1,100))
    if len(num2) < 10:
        num2.add(random.randint(1,100))
    if len(num1) == 10 and len(num2) == 10:
        break

print('발생된 10개의 난수 num1',num1)
print('발생된 10개의 난수 num2',num2)
print('num1,num2의 합세트',num1|num2)
print('num1,num2의 교세트',num1&num2)
print('num1,num2의 차세트',num1-num2)