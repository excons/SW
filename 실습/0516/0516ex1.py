'''
2023.05.16
김영빈
파일 입출력
'''

ft=open("D:/SW/실습/data/test.txt","w",encoding='utf-8')#파일 객체 생성(읽기)

for i in range(1,11):#10번 반복
    ft.write('%d번째 줄입니다.\n'%i)#ft에 i 출력

ft.close()#파일 종료