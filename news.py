import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# data = requests.get('https://news.naver.com/section/100') #크롤링 할 url data라는 변수에 가져오기
# soup = BeautifulSoup(data.content, 'html.parser') #soup 문법

# 헤드라인 = soup.select('div.sa_text a strong.sa_text_strong')[0].text #해석하면 div태그에 class가 "sa_text"의 하위요소 a태그의 하위요소 strong태그에 class가 sa_text_strong인 content
# print(len(헤드라인)) #len()은 그냥 리스트 자료형에 몇개의 자료가 있는지 
# print(헤드라인)

# 헤드라인_url = soup.select('div.sa_thumb_inner a')[0]
# # print(헤드라인_url['href'])


# data2 = requests.get(헤드라인_url['href'])
# soup = BeautifulSoup(data2.content, 'html.parser')

# 본문 = soup.select('article#dic_area')[0].text
# print(본문)

data = requests.get('https://finance.naver.com/item/news_news.nhn?code=005930&page=&sm=title_entity_id.basic&clusterId=') #크롤링 할 url data라는 변수에 가져오기
soup = BeautifulSoup(data.content, 'html.parser') #soup 문법

base_url = "https://finance.naver.com/item/news_news.nhn?code=005930&page=&sm=title_entity_id.basic&clusterId="  # 실제 페이지 URL의 도메인 부분
response = requests.get(base_url)

헤드라인 = soup.select('a.tit')[0] #해석하면 div태그에 class가 "sa_text"의 하위요소 a태그의 하위요소 strong태그에 class가 sa_text_strong인 content
print(헤드라인.text)

링크 = 헤드라인['href']
absolute_url = urljoin(base_url, 링크)
print(absolute_url)

본문data = requests.get(absolute_url)
soup2 = BeautifulSoup(data.content, 'html.parser')

본문 = soup2.select('article#dic_area')
print(본문)




exit()
헤드라인_url = soup.select('div.sa_thumb_inner a')[0]
# print(헤드라인_url['href'])


data2 = requests.get(헤드라인_url['href'])
soup = BeautifulSoup(data2.content, 'html.parser')

본문 = soup.select('article#dic_area')[0].text
print(본문)

