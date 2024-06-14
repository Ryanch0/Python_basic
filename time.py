import time

print(time.time()) #출력시 epoch time
epochTime = time.time()
시간 = time.ctime(epochTime) #읽기 쉬운 시간
print(시간)
시간 = time.localtime() #localtime() 원하는부분만 뽑아쓰기 가능
a = time.strftime('%Y year %m month',시간) #년월일시분초 쉽게 가능
print(a)
name = 'Kim'
print(f'안녕하세요 {name}') #변수삽입 formatting 문법
import datetime
a = datetime.datetime(2022, 10, 1) #간단하게 시간 표현 , 현재시간은 datetime.datetime.now()
print(a)