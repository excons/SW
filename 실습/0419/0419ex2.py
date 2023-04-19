'''
2023.04.18
김영빈
두번째
입력받은 숫자가 양수,0,음수 인지 구분
#문제분석
    변수:입력받은 숫자(num)
    수식
        num>0 양수
        num==0 0
        num<0 음수
#알고리즘(단순if)
    1.변수 선언
        num 에 정수입력
    2.논리(선택)
        if num > 0:
            print('입력값{}은(는) 양수입니다.'.format(num))
        if num == 0:
            print('입력값{}은(는) 0입니다.'.format(num))
        if num < 0:
            print('입력값{}은(는) 음수입니다.'.format(num))
#알고리즘(다중if)
    1.변수 선언
        num 에 정수입력
    2.논리(선택)
        if num > 0:
            print('입력값{}은(는) 양수입니다.'.format(num))
        elif num == 0:
            print('입력값{}은(는) 0입니다.'.format(num))
        else :
            print('입력값{}은(는) 음수입니다.'.format(num))
''' 

num = int(input('숫자 입력 : '))
'''
if num > 0:
    print('입력값{}은(는) 양수입니다.'.format(num))
if num == 0:
    print('입력값{}은(는) 0입니다.'.format(num))
if num < 0:
    print('입력값{}은(는) 음수입니다.'.format(num))
'''
if num > 0:
    print('입력값{}은(는) 양수입니다.'.format(num))
elif num == 0:
    print('입력값{}은(는) 0입니다.'.format(num))
else :
    print('입력값{}은(는) 음수입니다.'.format(num))