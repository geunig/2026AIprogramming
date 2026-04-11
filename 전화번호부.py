import json

addressbook = dict()

try:
    with open('addressbook.json', 'r',encoding='utf-8') as f:
        addressbook = json.load(f)
except:
    adressbook = {}

while True:
    name=input('이름을 입력하세요(종료하려면 끝 입력): ')
    if name == '끝':
        break
    phoneNum = input('전화번호를 입력하세요: ')
    addressbook[name] = phoneNum

    if name in addressbook:
        choice = input(f'"{name}"은 이미 존재합니다.')
        continue

with open('addressbook.json','w', encoding='utf-8') as f:
    json.dump(addressbook,f,ensure_ascii=False,indent=4)

print('주소록이 저장되었습니다.')

