'''
score = [87,84,95,67,88,94,63]
names = ['영호','순자','영식','순희', score]
adbook = [['영호','25','010-1234-0000'],['철수','23','010-1111-0000']]
for i in adbook:
    print(i)

ri = list(range(5))
print(ri)

myString = "apple"

for ch in myString:
    print(ch)

listString = list(myString)
print(listString)

n_list = [10,20,30,40]
n_list.append(50)
print(n_list)
n_list.remove(10)
print(n_list)

a = n_list.pop()
print(a)
print(n_list)

print(50 not in n_list)
print(10 in n_list)

list1 = [10, 30, 20]
list1.sort()
print(list1)
list1.sort(reverse=True)
print(list1)
# 이 시점에서 list가 바뀐 것이다.
list2 = sorted(list1)
print(list1)
print(list2)
'''

list3 = [1,2,3,4]
list4 = [2,3,4,5]
print(list3 < list4)

list5 = [10,20,30,40,50]
i = 0
for n in list5:
    list5[i] = n*10
    i = i+1
print(list5)

list5 = [n*10 for n in list5]
print(list5)


