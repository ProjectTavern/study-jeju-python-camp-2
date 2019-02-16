from selenium import webdriver
from selenium.webdriver.common.keys import Keys

path = "C:/crawling/chromedriver.exe"

#조금만 기다리면 selenium으로 제어할 수 있는 브라우저 새창이 뜬다
driver = webdriver.Chrome(path)

#webdriver가 google 페이지에 접속하도록 명령
driver.get('들어갈URL')

id = driver.find_element_by_id("emailInput")
pw = driver.find_element_by_id("passwordInput")

id.send_keys("아이디")
pw.send_keys("패스워드")


pw.send_keys(Keys.ENTER)

con = driver.find_element_by_id("status_btn_new_container")
con.click()

#webdriver를 종료하여 창이 사라진다
driver.close()
