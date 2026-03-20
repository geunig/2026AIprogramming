#2-1
print('나의 이름은 :', '홍길동')
print('나의 나이는 :',27)
print('나의 키는', 179,'cm 입니다.')
print('10 + 20 =', 10+20)
print('10 * 20 =', 10 *20)

#2-2,3
radius = 4.0
print('원의 반지름', radius)
print('원의 면적', 3.14*radius*radius)
print('원의 둘레', 2.0*3.14*radius)

#2-4
name = '전우치'
print('나의 이름은 :', name)
age = 27
print('나의 나이는 :', age)
height = 179
print('나의 키는', height, 'cm 입니다.')
summ=10+20
print('10 + 20 =', summ)
mult=10*20
print('10 * 20 =', mult)

#2-6
width = 20
height = 40
width = 30
area = width * height
print('사각형의 면적', area)

#2-7
print(123 * 456)
print(1357+2468)
print(5**4)
print(10/4)
print(10//5)
print(10%5)

print(5%2)
print(2**0.5)
print(3**0.5)

#2-8
a=8+2j
b=4+3j
print('a + b =', a+b)
print('a - b =', a-b)
print('a * b =', a*b)
print('a / b =', a/b)

#2-9
c=1024
print('c>>1=', c>>1)
print('c>>2=', c>>2)
c=c>>1
print('c=c>>1일때, c=', c)
c=c>>1
print('c=c>>1를 한번더 수행하면, c=', c)
c=1
print('c=1이라 하면, c<<1=', c<<1)
c=c<<1
print(c)
c=c<<1
print(c)
c=c<<1
print(c)
c=c<<1
print(c)

#2-9
name = input('이름을 입력하세요 : ')
print(name, '님이 입장하셨습니다.')

m=int(input('숫자 m을 입력하세요 :'))
n = int(input('숫자 n을 입력하세요 :'))
print('m+n =', m+n)
print('m-n =', m-n)

radius=int(input('원의 반지름을 입력하세요 :'))
print('원의 면적 =', 3.14*radius*radius)
