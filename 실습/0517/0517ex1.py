'''
2023.05.17
김영빈
for 문을 이용한 파일 읽기
'''

with open("D:/SW/실습/data/Line test.txt","r",encoding="utf-8") as f:#파일 읽기
    for line in f:#파일 객체를 지정해서 반복문 작성
        print(line,end='')#줄 바꿈 없이 출력

#readline():(한 줄씩 읽어 오기)메소드로 파일 읽어 오기
print()

with open("D:/SW/실습/data/Line test.txt","r",encoding="utf-8") as f:#파일 읽기
    while True:#무한 반복
        line=f.readline()#파일 한 줄씩 읽어 오기
        print(line,end='')#줄 바꿈 없이 출력

        if line == '':#읽어 올 내용이 없다면
            break#반복 종료

#readlines():한 줄씩 읽어서 리스트 형으로 반환
print()

with open("D:/SW/실습/data/Line test.txt","r",encoding="utf-8") as f:#파일 읽기
    textLists = f.readlines()#한 줄식 리스트 형식으로 읽어 오기

    print(type(textLists))#변수 타입 확인
    print(textLists)


f = open("D:/SW/실습/data/ptest.txt","w",encoding="utf-8") #쓰기 모드의 파일 객체 생성

print('aaaaaa',file=f)#파일에 출력
print('bbbbbb',file=f)#파일에 출력
print('cccccc',file=f)#파일에 출력

f.close()