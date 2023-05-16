'''
2023.05.16
김영빈
파일 입출력 - seek(0):파일의 처음으로 포인트 이동
           - read(int n):지정한 갯수만큼 파일 읽어오기
'''

f = open("D:/SW/실습/data/test.txt","r",encoding='utf-8')

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.seek(0)

print(f.read(10),end='')
print(f.read(10),end='')
print(f.read(10))

f.close()