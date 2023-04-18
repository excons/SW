'''
2023.04.18
김영빈
세번째
145쪽 07번
'''

x = int(input('x의 값을 입력해주세요 :'))
y = int(input('y의 값을 입력해주세요 :'))


if x > y:
    if y == 0:
        print('y의 값이 0 입니다')
    else:
        print(x,'//',y,'=',x//y)
elif x < y:
    print(x,'+',y,'=',x+y)
elif x == y:
    print(x,'*',y,'=',x*y)
