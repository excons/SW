'''
2023.05.16
김영빈
파일 입출력 - 읽기(read()-전체 내용을 하나의 문자열로 반환)
'''

f = open("D:/SW/실습/data/test.txt","r",encoding='utf-8')

txts = f.read()

print(txts)

f.close()