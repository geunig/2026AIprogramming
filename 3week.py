'''
num = 300
print('num = ', num)
'''
'''
num = 0
for i in range(100):
    num += 100
    print('ith num =',i, num)
'''
age = int(input("나이를 입력하세요:"))
if age < 20:
    print('청소년 할인')
elif age >= 65:
    print('경로 우대')
# else는 else:로 사용하며 위의 조건을 만족하지 않는 경우.
# elif는 if 조건 만족하지 않는 것들 중 특정 경우.

