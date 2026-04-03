
i = 0
while i<5:
    print('Welcome to everyone!')
    i += 1 # 이게 없으면 무한루프된다. 또는 while문에 속하지 않으면 무한루프된다

for i in range(5):
    print('Welcome!')

isum = 0
n_list = [0,2,5,10]
for i in n_list:
    isum += i
print(isum)

nlist = [0,2,5,10]
isum = 0
i = 0
while i<len(nlist):
    isum += nlist[i]
    i += 1
print(isum) #len이 없으면 리스트의 개수를 알아야한다는 단점이 있음

