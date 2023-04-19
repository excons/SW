'''
2023.04.18
김영빈
첫번째
성별,키,몸무게 를 입력받아 표준 체중 구하기
1.변수선언
    성별(sex), 키(height), 몸무게(weight) 평균(avg)
2.수식
    sex == m or M    
        avg = height*height*22
    sex == f of F
        avg = height*height*21
    weight/avg*100
3.논리
        if sex == 'm' or sex == 'M' :
            avg = height*height*22
            if 119 >= weight/avg * 100 >= 110:
                print('과체중')
            elif weight/avg * 100 >= 120:
                print('비만 체중')
            else : 
                print('표준')
                
        elif sex == 'f' or sex == 'F':    
            avg = height*height*21
            if 119 >= weight/avg * 100 >= 110:
                print('과체중')
            elif weight/avg * 100 >= 120:
                print('비만 체중')
            else : 
                print('표준')
        else:
            print('성별 입력이 잘못 되었습니다.')
'''

sex = input("성별 입력('M or m' 또는 'F or f'):")
height = float(input('키 입력(cm):'))*0.01
weight = float(input('몸무게 입력(kg):'))




if sex == 'm' or sex == 'M' :

    avg = height*height*22

    if 119 >= weight/avg * 100 >= 110:
        print('과체중')
    elif weight/avg * 100 >= 120:
        print('비만 체중')
    else : 
        print('표준')

elif sex == 'f' or sex == 'F':    

    avg = height*height*21

    if 119 >= weight/avg * 100 >= 110:
        print('과체중')
    elif weight/avg * 100 >= 120:
        print('비만 체중')
    else : 
        print('표준')

else:
    print('성별 입력이 잘못 되었습니다.')