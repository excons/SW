'''
2023.06.13
김영빈
문제정의
    하나의 숫자를 입력 받아서 1~입력받은 숫자사이의
    약수를 구하는 dunmber()함수 구현하기
알고리즘
    1.함수 dnumber()정의
        1.1 반복문 과 조건문을 사용해서 약수 구하기
    2.사용자로부터 변수 입력받기
    3.약수를 저장받을 리스트 생성
    4.함수 호출하여 입력받은 변수의 약수를 구하여 리스트에 저장
    5.리스트 출력
'''

def dnumber(num,num_list):
    for i in range(1,num+1):
        if num % i == 0:
            num_list.append(i)
        
num = int(input('자연수를 입력하세요 :'))

num_list = []

if num > 0:
    dnumber(num,num_list)
    print(num,'의 약수는 :',num_list)

else :
    print(num,'은 자연수가 아닙니다.')