import requests
from bs4 import BeautifulSoup

data = requests.get('https://news.naver.com/section/100')
soup = BeautifulSoup(data.content, 'html.parser')

헤드라인 = soup.select('div.sa_text a strong.sa_text_strong')[0].text
print(len(헤드라인))
print(헤드라인)

헤드라인_url = soup.select('div.sa_thumb_inner a')[0]
# print(헤드라인_url['href'])


data2 = requests.get(헤드라인_url['href'])
soup = BeautifulSoup(data2.content, 'html.parser')

본문 = soup.select('article#dic_area')[0].text
print(본문)


