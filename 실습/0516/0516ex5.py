'''
2023.05.16
김영빈
파일 입출력 - writelines()->리스트나 튜플 같은 자료형을 파일에 저장
            - wirte()-> 문자열만 파일에 출력
'''
#문자열 리스트
L1 = ['충청남도','충청북도\n','전라남도','전라북도\n','경상남도','경상북도\n']
#정수형 리스트
L2 = [1,2,3,4,5,6]
#with 구문으로 파일 객체 생성
with open("D:/SW/실습/data/Line test.txt","w",encoding="utf-8") as f:

    f.writelines(L1)
