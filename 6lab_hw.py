#6-1
capital_dic = {'Korea':'Seoul','China':'Beijing','USA':'Washington DC'}
print(capital_dic['Korea'])
print(capital_dic['China'])
print(capital_dic['USA'])

fruits_dic = {'apple':'5000','banana':'4000','grape':'5300','melon':'6500'}
for key,value in fruits_dic.items():
    print(f'{key}의 가격은 {value}원입니다.')

#6-2
person = {'이름':'홍길동','나이':'26','몸무게':'82'}
print(person)
person['특기'] = '분신술'
person['아버지'] = '홍판서'
del person['나이']
print(person)

#6-3
print('Korea' in capital_dic)
print('China' in capital_dic)
print('Indonesia' in capital_dic)
print('Beijing' in capital_dic)

#6-4
print(fruits_dic.keys())
print(fruits_dic.values())

#6-5
print(list(fruits_dic.keys()))
print(list(fruits_dic.values()))
print('fruits_dic 항목 개수:', len(fruits_dic))
for fruits in ['apple','mango']:
    if fruits in fruits_dic:
        print(f'{fruits}이(가) 있습니다.')
    else:
        print(f'{fruits}이(가) 없습니다.')
            
#6-6
theday = (1919,3,1)
year,month,day = theday
print(f'{year}년 {month}월 {day}일은 삼일절입니다.')

num = [10,20,30]
unpack=tuple(num)
c,b,a = unpack
print(f'a = {a}\n'
      f'b = {b}\n'
      f'c = {c}')

#6-7
man = ('홍길동', 2019001, 179)
print(man)
man_list = list(man)
man_list[1] = 2019003
man = tuple(man_list)
print('변경 후:',man)

#6-8
def square(x,y):
    return x**2, y**2
x = 10
y = 20

x_sq,y_sq = square(x,y)

print(f'{x}제곱 {x_sq}, {y}제곱 {y_sq}')

t0 = (10,20,30)
t1 = (40,50,60)
t2 = t0+t1
print(t2)

print('Hello ' * 3)
print(('Hello ',) * 3) # 문자열은 문자들의 연속. 튜플 반복은 새로운 튜플로 확장

#6-9
lst = ['apple','mango','banana']
s1 = set(lst)
print(s1)
greet = 'Good afternoon'
s2 = set(greet)
print(s2)

#6-10
a1 = {10,20,30,40}
a2 = {30,40,50,60,70}

print(f'합집합: {a1|a2}, 교집합: {a1&a2}, a1-a2 차집합: {a1-a2}\
 대칭차집합: {a1^a2}, a1은 a2의 부분집합인가? : {a1.issubset(a2)},\
 a1은 a2의 상위집합인가? : {a1.issuperset(a2)},\
 a1은 a2와 서로소인가? : {a1.isdisjoint(a2)} ')
