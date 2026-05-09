#9-1
#1) a = 100, b = 20000, c = 2.0
#2) 40, 3) get(), 4) & 5) 수행 완료.

#9-2
# 객체지향프로그래밍 : 설계된 클래스를 이용해 객체를 생성하며, 이들 간의
#                      상호작용으로 프로그램을 표현하고 소프트웨어를 개발한다.
# 절차적프로그래밍 : 함수와 모듈을 만들어 두고 문제해결 순서에 맞게 호출해
#                    수행한다. GUI 및 대규모 프로그램에서 구동이 어렵다.
# 그래픽사용자인터페이스 : 사용자가 시각적 요소를 통해 컴퓨터와 상호작용할 수
#                          있는 인터페이스.

# 절차적 프로그래밍은 함수와 실행 흐름을 중심으로 구동되며, 대규모 프로그램의
# 경우 필요한 함수가 크게 늘어난다. 반면 객체지향 프로그래밍은 각 객체를 설계해
# 그 객체들끼리 상호작용이 가능하므로, 유지보수 비용이 적게 든다.

#9-3
# 클래스 : 프로그램 상에서 사용되는 속성과 행위를 모아놓은 집합체
# 객체 : 클래스에 의해 만들어진 대상
# 인스턴스 : 클래스로부터 만들어지는 서로 다른 속성을 갖는 각각의 객체
# 클래스의 속성 : 객체가 가지는 데이터 및 상태
# 클래스의 동작 : 객체가 수행하는 기능이나 행동

#9-4, 9-5, 9-6
'''
class Dog:
    def __init__(self, name = '바둑이'):
        self.name = name

    def bark(self):
        print('내 이름은 {}, 멍멍~'.format(self.name))

    def __str__(self):
        return'{}의 정보 : Dog(name = {})'.format(self.name, self.name)

myDog = Dog('Jindo')
myDog.bark()
print(myDog)

# 9-7
n = 100
m = 100
if n is m:
    print('n is m')
else:
    print('n is not m') # 결과 : n is m


#9-8

class Vector2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __mul__(self, other):
        return Vector2D(self.x * other.x, self.y * other.y)
    def __truediv__(self, other):
        return Vector2D(self.x / other.x, self.y / other.y)
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    def __neg__(self):
        return Vector2D(-self.x, -self.y)

v1 = Vector2D(30,40)
v2 = Vector2D(10,20)
v3 = v1 * v2
print('v1 * v2 =', v3)
v4 = v1 / v2
print('v1 / v2 =', v4)
v5 = -v2
print('-v2 =', v5)


#9-9

class Compare:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __gt__(self, other):
        selfSize = ((self.x)**2 + (self.y)**2)**0.5
        otherSize = ((other.x)**2 + (other.y)**2)**0.5
        return selfSize > otherSize
    def __ge__(self, other):
        selfSize = ((self.x)**2 + (self.y)**2)**0.5
        otherSize = ((other.x)**2 + (other.y)**2)**0.5
        return selfSize >= otherSize
    def __lt__(self, other):
        selfSize = ((self.x)**2 + (self.y)**2)**0.5
        otherSize = ((other.x)**2 + (other.y)**2)**0.5
        return selfSize < otherSize
    def __le__(self, other):
        selfSize = ((self.x)**2 + (self.y)**2)**0.5
        otherSize = ((other.x)**2 + (other.y)**2)**0.5
        return selfSize <= otherSize

v1 = Compare(30,40)
v2 = Compare(10,20)
v3 = v1 > v2
print('v1 > v2 =', v3)
v4 = v1 >= v2
print('v1 >= v2 =', v4)
v5 = v1 < v2
print('v1 < v2 =', v5)
v6 = v1 <= v2
print('v1 <= v2 =', v6)


# 9-10
class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['width'])
'''
class Rect:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

r1 = Rect(100,200)
print(r1.__dict__)
print(r1.__dict__['_Rect__width'])














