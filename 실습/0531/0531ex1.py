'''
2023.05.31
김영빈
문제정의  
    -10개의 난수를 발생 시키고 리스트에 저장한후 최대 최소 합계 구하기
문제분석
    변수 - 빈리스트(num)
알고리즘
    1.랜덤 모듈 추가(import random)
    2.변수 초기화(num=[])
    3.반복(for i in range(10):난수 생성)
    4.결과 출력(최대,최소,합계,정렬)
'''

import random

num = []

for i in range(10):
    num.append(random.randint(1,100))

print('생성된 리스트 :',num)
print('가장 큰 값 :',max(num))
print('가장 작은 값 :',min(num))
print('전체 요소의 합 :',sum(num))
num.sort()
print('오름차순 리스트 :',num)
num.sort(reverse=True)
print('내림차순 리스트 :',num)