'''
2023.06.07
김영빈
문제정의
    5명의 학생의 학번과 전화번호를 입력받아 딕셔너리에 저장하고 학번을 입력하면 해당학생의 전화번호를 출력하라
문제분석
    변수 - 전화번호부(phone),학번(id),전화번호(pnum)
알고리즘
    1.전화번호 딕셔너리 생성
    2.학생의 학번,전화번호 입력(반복 for 5)
        2-1.학번,전화번호를 딕셔너리에 저장
    3.조건
        if id in phone
            해당 번호 출력
        else
            없음 출력
'''

phone = dict()

for i in range(5):
    id = int(input(str(i+1)+'번째 학생 학번 입력 :'))
    pnum = input(str(i+1)+'번째 학생 전화번호 입력 :')
    phone[id]=pnum

print('학생 전화번호부가 완성되었습니다.')

id = int(input('검색을 원하는 학생의 학번 입력 :'))

if id in phone:
    print("입력한 학생의 전화번호 :",phone[id])
else:
    print("입력한 학생의 전화번호가 없습니다.")