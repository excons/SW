'''
2023.05.17
김영빈
문제 정의
    학생의 이름과 성적을 받은 파일을 불러와서 학생들의 평균을 구하라
문제 분석
    변수
        파일내용(txts),파일리스트(txtlist),학생이름(name),합계(sum)
    수식
        sum = sum+int(txtlist[i]) 학생의 성적 총합
        sum/3 성적총합의 평균
알고리즘
    2.파일의 성적 평균
        1.stu.txt 파일 읽기
        2.파일의 내용을 txts에 저장
        3.학생의 이름을 리스트형으로 저장
        4.학생의 이름과 숫자를 구분
        5.숫자를 int형으로 전환하여 합계를 계산
        6.평균을 구하여 출력
'''

with open("D:/SW/실습/data/stu.txt","r",encoding='utf-8') as f:#파일 읽기
    while True:#무한반복
        txts = f.readline()#한줄씩 읽은후 저장
        if txts == '':#조건
            break#조건 만족시 종료
        txtlist = txts.split()#txts를 리스트형으로 전환
        name = txtlist[0]#이름 구분
        sum = 0#변수 초기화
        for i in range(1,4):#반복조건
            sum = sum+int(txtlist[i])#리스트 정수형 변환후 합계
        print(name,'의 평균 성적은 :',sum/3)#구분한 이름과 합계의 평균을 계산하여 출력
        