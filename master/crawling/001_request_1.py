#바울랩 크롤링 & 파일 입출력 & 단어 분석
#pip3 install requests
import requests

response = requests.get('바울랩URL')
print(response.encoding)
response.encoding = 'utf-8'
html = response.text
print(html)

f = open('test.html', 'w')
f.write(html)
f.close()

spliteHTML = html.split(' ')
print(spliteHTML)
print(spliteHTML.count('검색할 단어'))
#print(dir(requests))
