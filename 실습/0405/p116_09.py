'''
2023.04.05
김영빈
116쪽 09번문제
'''

pay = int(input('본봉 :'))
bonus = int(input('수당 :'))

total = pay + bonus

tax = total*0.2

receive = total - tax

print('홍길동의 이번 달 본봉은 {}이고 수당이{}일때 수령액은 {}이다'.format(pay,bonus,receive) )