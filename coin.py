import requests
import json
import time


data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/krw/eth?interval=15m')
#출력했을때 ""있으면 JSON자료형이다. ex) 딕셔너리 = {'name' : 'val'} / JSON = {"name" : "val"} 
딕셔너리 = json.loads(data.content) #JSON을 딕셔너리데이터로 바꾸기
#내 데이터는 {{[{데이터}]}} 이런형식이다

for i in range(200):
    시간 = 딕셔너리['body']['candles'][i]['dt']
    print(time.strftime('%Y-%m-%d %H:%M:%S',
     time.localtime(시간 / 1000))) #epoch시간 변환
    print(딕셔너리['body']['candles'][i]['close'])  #이런식으로 뽑는다
