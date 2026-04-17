'''
student1 = {'name':'민수','score':84}
student2 = {'name':'지영','score':92}

def get_grade(student):
    if student['score'] >= 90:
        return 'A'
    elif student['score'] >= 80:
        return 'B'
    else:
        return 'C'

print(get_grade(student1))
print(get_grade(student2))
'''
# __init__은 class를 초기화하는 함수
class Student:
    def __init__(self,name,score):
        self.__name = name
        self.__score = score

    def __str__(self):
        return(f'이름:{self.__name}, 점수:{self.__score}')


    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 80:
            return 'B'
        else:
            return 'C'

민수 = Student('민수',85) #딕셔너리보다 class 변수가 훨씬 간단하다.
지영 = Student('지영',91)

print(민수)
print(민수.get_grade())
print(지영)
print(지영.get_grade())
print(민수.__name)
'''
class Phone:
    def __init__(self, name, brand, battery):
        self.name = name
        self.brand = brand
        self.battery = battery
    def __str__(self):
        return f'(name = {self.name}, brand = {self.brand}, \
battery = {self.battery})'

    def use(self,minutes):
        self.battery -= 0.5 * minutes
        print('{}분 사용 후 배터리 잔량 ='.format(minutes),self.battery,'%')
    def charge(self,minutes):
        self.battery += 0.5 * minutes
        print('{}분 충전 후 배터리 잔량 ='.format(minutes),self.battery,'%')
my_phone = Phone('my_phone','galaxy',80)
print(my_phone)
my_phone.use(30)
my_phone.charge(60)
'''


        
