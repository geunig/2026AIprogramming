'''
#7-1
import datetime as dt

today = dt.datetime.today()
print('오늘의 날짜 :','{}년 {}월 {}일'.format(today.year,today.month,today.day))
time = dt.datetime.now()
if time.hour < 12:
    ampm = '오전'
    hour = time.hour
else:
    ampm = '오후'
    hour = time.hour-12
if hour == 0:
    hour = 12
print('현재 시간 : {} {}시 {}분 {}초'.format(ampm,hour,time.minute,time.second))

#7-2

print('오늘은 {}년 {}월 {}일 입니다.'.format(today.year,today.month,today.day))
dates = [
    ('2026년 크리스마스', dt.datetime(2026,12,25)),
    ('2036년 1월 1일', dt.datetime(2036,1,1)),
    ('2027년 4월 4일', dt.datetime(2027,4,4))]

for name,day in dates:
    gap = day-today
    print('{}까지는 {}일 {}시간 남았습니다'\
          .format(name, gap.days,gap.seconds//3600))

#7-3
after1000 = today + dt.timedelta(days=1000)
print('오늘 : ', today)
print('1000일 후 :', after1000)

year,month,day = input('처음으로 사귄 연도,월,일 입력(,구분): ')\
                               .split(',')
year = int(year)
month = int(month)
day = int(day)

start = dt.datetime(year,month,day)
day_100 = start + dt.timedelta(days=100)

print('사귄 날:', start)
print('100일 기념일은 {}년 {}월 {}일입니다.'.format(day_100.year,\
                                         day_100.month,day_100.day))

#7-4
import math

for i in range(2, 11):
    print(f'4**{i} = {math.pow(4, i)}')
    
for d in range(0, 181, 10):
    rad = d * math.pi / 180
    print(f'{d} degree = {rad:.3f} radian')

for d in range(0, 181, 10):
    rad = d * math.pi / 180
    print(f'sin({d}) = {math.sin(rad):.2f}')


#7-5
import random

multiple5 = list(range(0,101,5))
result1 = random.sample(multiple5,3)
print('0이상 100이하 정수 중 5의 배수 3개:', result1)
result2 = random.sample(range(1,11),3)
print('1에서 10사이의 임의의 정수 3개 :',result2)

#7-7
import turtle as t
t.shape("turtle")
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)

t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.done

#loop로 개선
import turtle as t
t.shape('turtle')
for _ in range(3):
    t.forward(100)
    t.left(120)

for _ in range(3):
    t.forward(200)
    t.left(120)
t.done

import turtle as t
t.shape('turtle')
triangle = [100,200,300]
for i in triangle:
    for j in range(3):
        t.forward(i)
        t.left(120)
t.done

for q in range(4):
    t.forward(100)
    t.left(90)

t.done()

#8-1
#1의 경우, IndexError 발생. 인덱스가 0,1,2만 있는데 3을 호출함.
#2의 경우, ValueError 발생. int로 변환할 수 없음.
#3의 경우, TypeError 발생. 정수와 문자열은 더할 수 없다.

try:
    a = [10, 20, 30]
    print(a[3])
except Exception as e:
    print(e)

try:
    n = int('20%')
except Exception as e:
    print(e)

try:
    a = 100 + '200'
except Exception as e:
    print(e)

#8-2
try:
    result = 10 * (30 / 0)
except ZeroDivisionError:
    print("0으로 나눗셈 시도함.")

try:
    x = int(input('정수 x를 입력하세요: '))
except ValueError:
    print("정수를 입력하지 않음.")

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
except FileNotFoundError:
    print("파일이 존재하지 않음.")
'''
#8-3
a = [1, 2, 3, 4, 5]
print(a)
try:
    x = int(input("a의 요소를 하나 선택하세요 : "))
    index = a.index(x)
    print(f"{x} 은(는) {index+1} 번째 요소입니다.")

except ValueError:
    print('입력값이 잘못되었습니다.')
