#3-6
for i in range(5):
    print('Hello, Python!')

for i in range(5):
    print(i)
#3-7
r = list(range(1,101))
print(r)
even = list(range(2,101,2))
print(even)
odd = list(range(1,101,2))
print(odd)
minus = list(range(0,-101,-1))
print(minus[::-1])

#3-8
s = 0
for i in range(1, 101):
    s = s + i
print('1에서 100까지의 합:', s)

n = 0
for i in range(0, 101, 2):
    n = n + i
print('1에서 100까지 짝수의 합:', n)

k = 0
for i in range(1, 101, 2):
    k = k + i
print('1에서 100까지 홀수의 합:', k)

#3-8
n = 7
for i in range(n):
    print(' ' * (n-i-1) + '#')
