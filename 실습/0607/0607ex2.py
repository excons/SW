'''
2023.06.07
김영빈
문제정의
    1~45사이의 숫자를 랜덤으로 6개 받아와서 오름차순으로 정렬하고 중복된 난수도 출력
문제분석
    변수-빈세트(num),난수저장(count)
알고리즘
    1.랜덤모듈 추가
    2.비어있는 세트 변수 생성
    3.난수채크할 변수 생성(count)
    4.반복(while True)
        num=랜덤수 추가(1~45)
        count+=1
        4-2.조건문
            num 이 6개가 대면 반복문 종료
    5.출력
'''

import random

num = set()
count=0

while True:
    num.add(random.randint(1,45))
    count+=1
    if len(num)== 6:
        break

print('이번주 로또 넘버 :',sorted(num))
print('중복된 난수의 발생 횟수',count-6)