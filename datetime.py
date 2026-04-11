import datetime as dt

print(dt.datetime.now())

today = dt.date.today()
print(today)
print(today.year)
print(today.day)

start_time = dt.datetime.now()
print(start_time.replace(month=12,day=25))
print(today)

print('오늘은 {}년 {}월 {}일 입니다.'.format(today.year,today.month,today.day))
xMas = dt.datetime(today.year,12,25)
# 26년 12월 26일이면 어떻게 해결할까?

if today>xMas:
    xMas = dt.datetime(today.year+1,12,25)

timeGap = xMas - dt.datetime.now()
print('다음 크리스마스까지는 {}일 {}시간 남았습니다'.format(\
    timeGap.days, timeGap.seconds // 3600))
# 숫자가 아니어도 더하고 뺄 수 있다.
