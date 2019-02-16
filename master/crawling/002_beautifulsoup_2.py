#pip3 install requests
#pip3 install beautifulsoup4
import requests
from bs4 import BeautifulSoup

response = requests.get('바울랩URL')

response.encoding = 'utf-8'
html = response.text
#print(html)

soup = BeautifulSoup(html, 'html.parser')
l = []
for tag in soup.select('.title_text'):
    l.append(tag.text.strip())

print(l)

for i, j in enumerate(l, 1):
    print(i, j)
    
x = ['하나', '둘', '셋']
for i in x:
    print(i)
    
x = [('하나', 0), ('둘', 1), ('셋', 2)]   
for i, j in x:
    print(i)   
    