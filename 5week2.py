'''
n = int(input('수를 입력하세요:'))
fact = 1 #곱하기는 기본값을 0으로 두면 안된다.
for i in range(1, n+1):
    fact = fact*i
print('{}! = {}'.format(n,fact))

summer_fruits=['수박','참외','체리','포도']
for fruits in summer_fruits:
    print(fruits, end = ' ')

for i in range(2,10):
    for j in range(1,10):
        print('{}*{} = {:2d}'.format(i,j,i*j), end = ' ')
    print() #아무것도 안 쓰고 줄바꿈하는 기능

n = 7
for i in range(n):
    st = ''
    for j in range(i):
        st = st+' '
    print(st + '#')

n = 7
for i in range(n):
    print(' '*i + '#')

n = int(input('수를 입력하세요:'))
isPrime = True
for num in range(2, n):
    if n % num ==0:
        isPrime = False
print(n, 'isPrime :',isPrime)

# 비효율적인 이유 : false 한번 나오면 더이상 수행할 필요가 없음
# 추가로, 7을 판별할 때 7의 절반보다 작은 수로 안 나눠지면,
# 절반보다 큰 수로 7을 나눠도 안 나눠지기 때문에 연산을 할 필요가 없다
'''

n = int(input('수를 입력하세요: '))
isPrime = True

for num in range(2, n // 2 + 1):   # 절반까지만 검사
    if n % num == 0:
        isPrime = False
        break                       # 더 검사할 필요 없음

print(n, 'isPrime :', isPrime)
