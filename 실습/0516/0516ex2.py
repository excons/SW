'''
2023.05.16
김영빈
파일 입출력 - 추가하기
'''

f=open("D:/SW/실습/data/test.txt","a",encoding="utf-8")#파일 객체 생성(추가)

f.write("마지막 줄 입니다.")#파일의 마지막에 추가

f.close()