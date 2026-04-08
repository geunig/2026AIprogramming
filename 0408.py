person = {'이름':'홍길동','나이':'26','몸무게':'82'}
print(person['이름'])
print(person['나이'])
print(person['몸무게'])

students = {'001':'이순신','002':'김유신','003':'강감찬'}
print(students['001'])
print(students['002'])
print(students['003'])

person['국적']='대한민국'
print(person)

# input으로 값을 받고 dictionary 변수에 3개까지 등록하라는 과제.
# 또는 특정 값을 받으면 중단하는 것도 해봐라. End of input 지정

# 파이썬에서 모든 변수는 객체변수class이다.

print(person.values())

for key in person:
    print('{} : {}'.format(key, person[key]))
# {}는 place_holder, 위치를 고정해준다.

tuple1 = (1,2,3)
print(tuple1[0])

def plusminus(a1,a2):
    return a1+a2, a1-a2
output = plusminus(10,2)
output_list = list(output) #이걸 통해 튜플 변수를 리스트 변수로 바꿀 수 있다.
print(type(output_list))
print(type(output))

a=100
b=200
print('swap 이전: a=', a, 'b=',b)
a,b = b,a
print('swap 이후: a=',a,'b=',b)


set1 = {0,5,2,2,4,1}
print(set1)
aset = {1,2,3,4}
bset = {2,4,6,7}
cset = aset.intersection(bset) #순서 바꿔도 가능
print(cset)
