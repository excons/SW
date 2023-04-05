'''
2023.04.05
김영빈
117쪽 14번문제
'''

sub1 = int(input('과목1의 점수는 :'))
sub2 = int(input('과목2의 점수는 :'))
sub3 = int(input('과목3의 점수는 :'))
sub4 = int(input('과목4의 점수는 :'))
sub5 = int(input('과목5의 점수는 :'))

total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total/5

print('5과목의 합계는 {}이고, 평균은 {}이다.'.format(total,avg))
