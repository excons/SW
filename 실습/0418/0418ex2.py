'''
2023.04.18
김영빈
두번째
두 과목 모두 75이상 그리고 총점 180이상 "최우수",
총점 160이상 "우수", 150이상 "보통"
두 과목 중 하나라도 75 미만이면 "분발"
#문제분석
    변수:점수1(num1),점수2(num2),합계(total)
    수식:total = num1 + num2
#알고리즘
    1.변수선언
        num1,num2에 점수 입력받기
        두 점수의 합을 total에 저장
    2.논리(선택-중첩if)
        if num1 >= 75 and num2 >= 75:
            if total >= 180:
                print('최우수 학생')
            elif total >= 160:
                print('우수 학생')
            else:
                print('보통 학생')
        else:
            print('분발합시다')
'''

num1 = int(input('첫 번째 과목의 점수 입력 :'))
num2 = int(input('두 번째 과목의 점수 입력 :'))

total = num1 + num2

if num1 >= 75 and num2 >= 75:
    if total >= 180:
        print('최우수 학생')
    elif total >= 160:
        print('우수 학생')
    else:
        print('보통 학생')
else:
    print('분발합시다')