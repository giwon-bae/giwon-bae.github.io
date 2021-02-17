```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib.request

driver = webdriver.Chrome()
driver.get("https://www.google.com")
elem = driver.find_element_by_name("q")
elem.send_keys("셀트리온헬스케어")
elem.send_keys(Keys.RETURN)
driver.find_element_by_class_name('hide-focus-ring').click()
time.sleep(1)
driver.find_elements_by_css_selector(".JheGif.nDgy9d")[0].click()
```
조코딩(JoCoding)님의 파이썬 셀레니움 이미지 크롤링 영상을 보고 학습한 후에 이를 참고하여 뉴스를 찾는 프로그램을 만들어 봤다.
새로운 뉴스가 올라올 때마다 저장하는 방식으로 만들 계획이었지만 아직 학습 내용에 대해 완전히 이해하지 못했기 때문에 좀 더 공부하고 차차 발전 시켜 나갈 것이다.
