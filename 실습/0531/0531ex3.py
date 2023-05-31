'''
2023.05.31
김영빈
문제정의
    두개의 튜플을 하나의 리스트로 합치기
문제분석
    변수-빈 리스트(fp_list)
알고리즘
    1.튜플정의
    2.빈 리스트 생성
    3.반복(두개의 튜플을 하나의 리스트로 합치기)
        for i in range(len(fruit)):
            fp_list.append(fruit[i])
            fp_list.append(price[i])
'''

fruit=('사과','배','파인애플','포도')
price=('5000','7000','4500','6000')

fp_list=[]

for i in range(len(fruit)):
    fp_list.append(fruit[i])
    fp_list.append(price[i])

print('과일 튜플 :',fruit)
print('가격 튜플 :',price)
print('튜플로부터 생성된 과일+가격 리스트 :',fp_list)