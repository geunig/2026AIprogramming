'''
while True:
    try:
        a,b = map(int,input('두 수를 입력하시오\
(두 수는 ,로 구분) :').split(','))
        result = a/b
        print(f'{a}/{b} = {result}')
        break
    except:
        print('수가 정확한지 확인하세요')


a,b,c = map(int,input('세 개의 숫자를 입력하세요(,로 구분):').split(','))
print(a,b,c)
# int는 단위 숫자는 정수로 바꿀 수 있지만, 리스트는 바꿀 수 없다.->map 사용
# split()은 문자열에 속한 함수이다.'1 2 3'.split()도 가능한데, class변수이기 때문.
'''
class Cat:
    def __init__(self, name, color='흰색'):
        self.name = name
        self.color = color

    def meow(self):
        print(f'내 이름은 {self.name}, 색깔은 {self.color}, 야옹~')

nabi = Cat('나비','검정색')
nero = Cat('네로','흰색')
mimi = Cat('미미','갈색')
momo = Cat('모모') 

nabi.meow()
nero.meow()
mimi.meow()
momo.meow()
