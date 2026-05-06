'''
class Rectangle:
    def __init__(self, side=0):
        self.side = side
    def getArea(self):
        return self.side * self.side

def printAreas(r,n):
    while n >= 1:
        print(r.side, '\t', r.getArea())
        r.side = r.side + 1
        n = n - 1

myRect = Rectangle();
count = 5
printAreas(myRect, count)
print('사각형의 변 =', myRect.side)
print('반복횟수 =', count)

class Television:
    serialNumber = 0

    def __init__(self):
        Television.serialNumber += 1
        self.number = Television.serialNumber

    def __str__(self):
        return '{}'.format(self.number)

t1 = Television()
t2 = Television()
myTv = Television()

print(t1,t2,myTv)

class Car:

    def __init__(self,name="",speed=0):
        self.name = name
        self.speed = speed

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def __str__(self):
        return '%s의 현재 속도는 %d입니다.'%(self.name,self.speed)

    def speedup(self,value):
        self.speed += value

    def speeddown(self,value):
        self.speed -= value

class Sedan(Car):

    def speedup(self, value):
        self.speed += value

        if self.speed > 150:
            self.speed = 150

    def speeddown(self,value):
        self.speed -= value

        if self.speed < 0:
            self.speed = 0
            print('차량의 속도는 0 이하가 될 수 없습니다!')

car1 = Sedan('K5', 50)
print(car1)
car1.speeddown(60)
print(car1)

class Line:
    length = 0
    def __init__(self,name,length):
        self.name = name
        self.length = length
        print(self.length,'길이의 선이 생성되었습니다.')
    def __del__(self):
        print(self.length,'길이의 선이 삭제되었습니다.')
    def __repr__(self):
        return '{} 선의 길이 : {} '.format(self.name, self.length)
    def __add__(self, other):
        return Line(self.name + '+' + other.name, self.length + other.length)
    def __lt__(self, other):
        return self.length < other.length
    def __eq__(self, other):
        return self.length == other.length

line1 = Line('line1', 100)
line2 = Line('line2', 200)
print(line1, line2)
print('두 선의 길이 합 : ', line1+line2)
if line1<line2:
    print('선분 2가 더 기네요.')
elif line1==line2:
    print('두 선분이 같네요.')
else:
    print('모르겠네요.')

print(type(Line))
print(type(line1))
result = line1 + line2
print(type(result))
'''
import threading
import time
import multiprocessing

class RacingCar:
    carName = ''
    def __init__(self, name):
        self.carName = name

    def runCar(self):
        for _ in range(3):
            print(self.carName + '~~달립니다.')
            time.sleep(0.1)

def run_wrapper(name):
    car = RacingCar(name)
    car.runCar()
    
if __name__ == "__main__":
    multiprocessing.freeze_support()
    mp1 = multiprocessing.Process(target=run_wrapper, args=('자동차1',))
    mp2 = multiprocessing.Process(target=run_wrapper, args=('자동차2',))
    mp3 = multiprocessing.Process(target=run_wrapper, args=('자동차3',))

    mp1.start()
    mp2.start()
    mp3.start()

    mp1.join()
    mp2.join()
    mp3.join()

'''
th1 = threading.Thread(target = car1.runCar)
th2 = threading.Thread(target = car2.runCar)
th3 = threading.Thread(target = car3.runCar)

th1.start()
th2.start()
th3.start()

car1.runCar()
car2.runCar()
car3.runCar()
'''


