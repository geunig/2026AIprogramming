#4-1 ~ 4-4
def print_star():
    print('*******')
# 함수 삭제 시 정의된 함수가 없다고 나온다.

for i in range(6):
    print_star()

def print_plus():
    print('+++')

for i in range(10):
    print_plus()

def print_hash():
    print('#####')

print_hash()
print_star()
print_plus()
print_plus()
print_star()
print_hash()

def print_at(n):
    for _ in range(n):
        print(_,'@@@')
print_at(10)

#4-5
def print_sub(a,b):
    result = a-b
    print(a,'과', b, '의 차는', result,'입니다.')
print_sub(10,20)

def print_mult(a,b):
    result = a*b
    print(a,'과', b, '의 곱은', result,'입니다.')
print_mult(10,20)

#4-6
def print_root(a, b, c):
    r1 = (-b + (b ** 2- 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b- (b ** 2- 4 * a * c) ** 0.5) / (2 * a)
    print('해는', r1, '또는', r2)

print_root(1.0,4.0,-21.0)
print_root(1.0,-6.0,8.0)

def print_area(a,b):
    result = a*b*0.5
    print('밑변 ',a,'높이 ',b,'인 삼각형의 면적은 ',result)

print_area(10,20)

#4-7
radius = int(input('원의 반지름 : '))

def circle_area_circum(radius):
    area = radius**2 * 3.14
    circum = 2 * radius * 3.14
    return area, circum
result1,result2 = circle_area_circum(radius)
print('반지름', radius,'인 원의 면적은', result1, '원둘레는', result2,'입니다')

#4-8
def multiply(n,m):
    return[n*i for i in range(1, m+1)]

r1,r2,r3,r4 = multiply(3,4)
print(r1,r2,r3,r4)

#4-9
def print_name(honorifics, first_name, last_name):
    '''키워드 인자를 이용한 출력용 프로그램'''
    print(honorifics, first_name, last_name)

print_name(first_name='Gildong', last_name='Hong', honorifics='Dr.')
print_name('Gildong','Hong','Dr.')


