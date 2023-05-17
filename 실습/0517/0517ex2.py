'''
2023.05.17
김영빈
#문제 정의
    기존 파일을 새로운 파일에 복사 하는 프로그램 만들기
#문제 분석
    변수 : 원본파일 입력(source), 복사할파일(target)
            원본파일의 내용(txts)
#알고리즘
    1.source에 원본 파일 이름 입력
    2.target에 복사할 파일 이름 입력
    3.파일처리
        source 파일 객체 생성
            파일 내용을 읽어와 txts 에 저장
        target 파일 객체 생성
            txts의 내용을 파일에 저장
'''

source = input('source 파일 입력 :')#원본 파일 이름
target = input('target 파일 입력 :')#복사할 파일 이름

with open(source, "r",encoding='utf-8') as f:#입력받은 원본파일 읽기 
    txts = f.read()#원본파일의 내용을 txts에 저장

with open(target,"w",encoding='utf-8') as cf:#입력받은 복사할 파일 을 생성후 쓰기
    cf.write(txts)#txts에 저장한 내용을 파일에 저장

    print(target,"파일이 생성되었습니다.")