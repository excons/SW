'''
2023.05.31
김영빈
문제정의
    튜플 안에 있는 숫자들의 종류와 반복 갯수 분석하기
문제분석
    빈 리스트(num_list)
알고리즘
    1.주어진 튜플 생성
    2.빈 리스트 생성
    3.반복조건
    4.조건문 생성
'''

num = (1,4,6,5,4,3,2,0,1,2,4,6,7,9,4,0)
print('생성된 튜플 :',num)
num_list = []

for i in range(len(num)) :
    if num[i] not in num_list:
        print(num[i],'개수 :',num.count(num[i]))
        num_list.append(num[i])

