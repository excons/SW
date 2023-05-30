'''
2023.05.30
김영빈
#문제 정의
    2차원 리스트의 각 줄의 합계를 구하고 리스트에서 가장 작은 값 찾기
'''

list1 = [[11,33,22,7],[77,2,90],[3,66,44,9,8]]

minvalue = min(list1[0])#minvalue 에 최소값 초기화

for i in range(len(list1)):#list1의 길이(3)만큼 반복
    print(i+1,'번째 줄의 합 :',sum(list1[i]))#각 줄의 합계


    if minvalue > min(list1[i]):#minvalue와 list1의 요소들을 비교
        minvalue = min(list1[i])#list1의 값이 작다면 값을 저장
    
print('리스트에서 가장 작은 값 :',minvalue)