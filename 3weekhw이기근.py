#3-1

game_score = int(input("게임 점수를 입력하세요: "))
if game_score > 1000:
    print('당신은 고수입니다.')

allowed_a=[100,300]
allowed_b=[200,300]
while True:
    num_a = int(input('a 값에 100 또는 300을 입력하세요: '))
    if num_a in allowed_a:
        break
    else:
        print('다시 입력하세요.')
print('a 입력 완료')

while True:
    num_b = int(input('b 값에 200 또는 300을 입력하세요: '))
    if num_b in allowed_b:
        break
    else:
        print('다시 입력하세요.')
print('b 입력 완료')

if num_a==num_b:
    print('두 값이 일치합니다.')
else:
    print('두 값이 다릅니다.')

#3-2

while True:
    try:
        n = int(input('1~100 사이의 정수를 입력하세요 :'))

        if 1<=n<=100:
            break
        else:
            print('1~100 사이 정수만 입력하세요.')
    except ValueError:
        print('숫자만 입력하세요!')

print('입력완료. n =', n)

if n % 2 == 0:
    print(n, '은(는) 짝수입니다.')
else:
    print(n, '은(는) 홀수입니다.')

#3-3
score = int(input('게임 점수를 입력하세요: '))
if score > 1000:
    print('고수입니다.')
else:
    print('입문자입니다.')

while True:
    try:
        age = int(input('당신은 성인인가요(성인이면 1, 미성년이면 0): '))
        if age not in (0,1):
            print('0 또는 1만 입력하세요.')
            continue
        if age == 0:
            print('당신은 미성년자입니다.')
        elif age == 1:
            print('당신은 성인입니다.')
            marriage = int(input('결혼을 하셨나요(기혼 1, 미혼 0): '))
            if marriage not in (0,1):
                print('0 또는 1만 입력하세요.')
                continue
            if marriage == 0:
                print('당신은 미혼 성인입니다.')
            elif marriage == 1:
                print('당신은 기혼 성인입니다.')
        print('작업 완료.')
        break
    except ValueError:
        print('올바른 값을 입력하세요!')

#3-4
num = int(input('1과 10 사이의 숫자를 입력하세요: '))
print(1<num and num<10)

age = int(input('나이를 입력하세요:'))
if age > 10 and age < 19:
    print('청소년입니다')
else:
    print('청소년이 아닙니다')


#3-5
speed = int(input('자동차 속도를 입력하세요(정수, km/h): '))
if speed>=100:
    print('고속')
elif speed>=60:
    print('중속')
else:
    print('저속')
