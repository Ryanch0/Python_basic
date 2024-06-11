#웹 크롤러 세팅
import requests  #파이썬으로 웹 접속 라이브러리
from bs4 import BeautifulSoup #html분석 라이브러리


def 크롤링(코드):
    data = requests.get(f'https://finance.naver.com/item/main.naver?code={코드}')
    # print(data.content) #data내용출력}
    # print(data.status_code) #200떠야 정상작동
    soup = BeautifulSoup(data.content, 'html.parser')
    # print(soup.find_all('em', class_='f_down')[0].text) #태그명, 클래스or id 등 으로 찾기
    # print(soup.select('em.f_down')) #select 문법
    # print(soup.select('.f_down em')[0].text) #띄어쓰기는 하위요소 
    # img = soup.select('img#img_chart_area')[0]
    # print(img['src']) #이미지 src 추출
    현재가 = soup.select('p.no_today em')
    for element in 현재가:
     for blind in element.find_all(class_='blind'):
        blind.decompose()
    return 현재가[0].text

종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']

f = open('a.text', 'w')
for i in 종목들:
    f.write(크롤링(i) + '\n')
f.close()
