#5-1

even_list = [2,4,6,8,10]
print(even_list)

even_list = list(range(2,12,2))
print(even_list)

nations = ['Korea','China','India','Nepal']
print(nations)

friends = ['길동','철수','은지','지은','영민']
print(friends)

string = list("XYZ")
print(string)

#5-2
prime_list=[2,3,5,7]
print('첫번째 원소:',prime_list[0])

print('마지막  원소:',prime_list[3])
print('마지막  원소:',prime_list[-1])
nations=['Korea','China','Russia','Malaysia']
print('첫째 원소:', nations[0])
print('마지막 원소', nations[-1])
print('마지막 원소', nations[len(nations)-1])

#5-3
prime = [2,3,5,7]
print('추가 전:', prime)
prime.append(11)
print('11 추가 후:',prime)
prime.remove(3)
print('3 삭제 후:', prime)
nations = ['Korea','China','Russia','Malaysia'] 
print('국가 목록:', nations)
nations.append('Nepal')
print('Nepal 추가 후:', nations)
if ('Japan' not in nations):
    print('Japan은 목록에 없습니다.')
if('Russia' in nations):
    print('Russia는 목록에 있습니다.')
#5-4
prime_list=[2,3,5,7]
print('최솟값:', min(prime_list))
print('최댓값:', max(prime_list))
print('합계:', sum(prime_list))
print('평균:', (sum(prime_list)/len(prime_list)))

nations = ['Korea','China','Russia','Malaysia']
print('사전에 가장 먼저 나옴:', nations[1])
print('사전에 가장 나중에 나옴', nations[2])

#5-5
a = [1,2,3]
b = [10,20,30]
a.append(b)
print(a)
a = [1,2,3]
a.extend(b)
print(a)
n_list = [1,2,3,4,5,6,7,8,9,10]
print(n_list)
n_list.insert(0,0)
print(n_list)
n_list.reverse()
print(n_list)
print('마지막 원소:',n_list.pop())
print(n_list)

#5-6
list1 = [1,2,3]
print(list1)
while True:
    try:
        n = int(input('반복할 정수를 입력하세요:'))
        print('list1 * n =' ,list1 * n)
        break
    except ValueError:
        print('올바른 값을 입력하세요!')

#5-7
list2 = list(range(0,15))
print(list2)
print(list2[:5])
print(list2[5:11])
print(list2[11:])
print(list2[2:11:2])
print(list2[10:5:-1])
print(list2[10:1:-2])
