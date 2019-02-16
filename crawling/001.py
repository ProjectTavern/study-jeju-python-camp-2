# pip3 install requests
# pip3 install beautifulsoup4
import requests
from bs4 import BeautifulSoup

response = requests.get('https://ridibooks.com/category/bestsellers/2200')
response.encoding = 'utf-8'
html = response.text

# print(html)

soup = BeautifulSoup(html, 'html.parser')
list = []

for tag in soup.select('.title_text'):
    list.append(tag.text.strip())

for i, j in enumerate(list, 1):
    print(i, j)

# 1. 자바스크립트에서 동적으로 할 경우
# 2. CAPTCHA 해결 방법
# 3. 인증이 필요한 것
