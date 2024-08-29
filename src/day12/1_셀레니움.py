# 1. 모듈 가져오기
from selenium import webdriver
# 2. webdriver 객체 생성
wd = webdriver.Chrome()

# 3.webdriver 객체를 이용한 웹페이지 접근 , get(URL)
wd.get("http://hanbit.co.kr")
