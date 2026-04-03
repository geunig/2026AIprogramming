
# 원하는 값이 입력되어야 실행되는 반복문
selected = None #문자열이라 None으로 두었고, 0으로 해도 코드는 실행된다.
while selected not in ['가위','바위','보']:
    selected = input('가위, 바위, 보 중에서 선택하세요:')
print('선택한 값은:', selected)

st = 'Programming'
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
    print(ch)
print('종료되었습니다.')

