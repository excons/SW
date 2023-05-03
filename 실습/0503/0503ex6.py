'''
2023.05.03
김영빈
2단부터 9단까지 전부 출력
#문제 정의
    구구단 출력(중첩 반복)
#문제 분석
    변수 i,j
#알고리즘
    논리(반복-중첩 반복(for))
    (조건)for i in range(2,10):
            print('**',i,'단 **')
            for j in range(1,10):
                print(i,'*',j,'=',i*j)
            print()
'''

for i in range(2,10):
    print('**',i,'단 **')#i단 구구단 제목출력
    for j in range(1,10):
        print(i,'*',j,'=',i*j)#i단 구구단을 출력
    print()#단 끝나고 줄띄움