'''
#end가 없으면 기본적으로 줄바꿈 기호가 들어간다.
#end가 있으면 줄바꿈 기호 대신 사용될 수 있다.
for i in range(5):
    print(i, end =' ')

for i in range(0,10,2):
    print(i, end=' ')

for i in range(-2, -10, -2):
    print(i, end = ' ')

#.뒤에는 method, behavior, etc.
s = 0
for i in range(1, 11):
    s=s+i
    print('i = {}, s = {}'.format(i,s) )
print('1에서 10까지의 합:', s)

n = int(input('합계를 구할 수를 입력:'))
s = 0

for i in range(0, n):
    s = s+(i+1) #n까지 end로 두면 n-1까지만 수행한다.
    #(i+1)을 해서 n까지 구할 수 있게 하다
print('1부터 {}까지의 합은 {}'.format(n,s))
'''
