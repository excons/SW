'''
2023.05.03
김영빈
#문제정의
    입력반은 구구단 출력 하기
#문제분석
    변수-반복할변수(i),단(dan)
#알고리즘
    1.변수선언
        dan은 정수로 입력
        i=1
    2.논리
        whlie i<=9:
            print(dan'*'i=dan*i)
            i+=1
'''

dan = int(input('숫자 입력 :'))
print('##',dan,'단 ##')
i=1
while i <= 9:
    print(dan,'*',i,'=',dan*i)
    i+=1