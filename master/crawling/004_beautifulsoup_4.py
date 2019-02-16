#공식홈페이지_SampleCode
from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.prettify())
#HTML이 다듬어져 나옵니다.
