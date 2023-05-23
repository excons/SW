'''
2023.05.23
김영빈
#문제정의
    키보드로 입력받은 내용을 리스트에 저장하고 파일(out.txt)에 저장하기
#문제분석
    변수-리스트(),입력값()
#알고리즘
    1.변수 초기화
        data[]
    2.파일 열기 객체 생성(쓰기)
    3.파일 처리
        3.1 (반복)while True:
                    text=문장입력
                    (선택)if txet=''
                            break
                    text를 data(리스트 변수) 추가
        3.2 파일에 결과 출력(writelines)
    4.파일 종료
                    
'''

data=[]

while True:
    text = input('저장할 문장입력(끝:엔터키) :')
    if text=='':
        break
    data.append(text+'\n')
print('입력될 리스트 :',data)

f=open("D:/SW/실습/data/out.txt","w",encoding='utf-8')

f.writelines(data)

f.close()

print('out.txt 파일이 생성되었습니다.')