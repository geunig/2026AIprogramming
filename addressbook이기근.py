import json

addressbook = {}

try:
    with open('addressbook.json', 'r', encoding='utf-8') as f:
        addressbook = json.load(f)
except:
    addressbook = {}

# 메뉴
while True:
    print('\n---- 주소록 ----')
    print('1. 연락처 추가')
    print('2. 연락처 삭제')
    print('3. 목록 보기')
    print('4. 종료')

    menu = input('메뉴를 선택하세요: ')

    if menu == '1':
        name = input('이름을 입력하세요: ')
        phoneNum = input('전화번호를 입력하세요: ')

        if name in addressbook:
            choice = input(f'"{name}"은(는) 이미 있습니다. 수정하려면 y: ')
            if choice.lower() != 'y':
                print('저장하지 않았습니다.')
                continue

        addressbook[name] = phoneNum
        print('저장되었습니다.')

    elif menu == '2':
        name = input('삭제할 이름을 입력하세요: ')
        if name in addressbook:
            del addressbook[name]
            print('삭제되었습니다.')
        else:
            print('해당 이름이 없습니다.')

    elif menu == '3':
        print('\n[주소록 목록]')
        for name, phone in addressbook.items():
            print(f'{name} : {phone}')

    elif menu == '4':
        break

    else:
        print('잘못된 입력입니다.')

with open('addressbook.json', 'w', encoding='utf-8') as f:
    json.dump(addressbook, f, ensure_ascii=False, indent=4)

print('주소록이 저장되었습니다.')
