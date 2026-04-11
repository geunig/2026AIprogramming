import json
'''
addressbook = {
    "김영호":"01047278728",
    "김수빈":"01020003000"}

with open('addressbook.json','w', encoding='utf-8') as f:
    json.dump(addressbook,f,ensure_ascii=False,indent=4)

print('주소록이 저장되었습니다.')
'''
with open('addressbook.json','r',encoding='utf-8') as f:
    addressbook=json.load(f)

print('불러온 주소록:', addressbook)
print('김영호 번호', addressbook['김영호'])

