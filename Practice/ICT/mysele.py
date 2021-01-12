from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/osangjin/Desktop/dev/Algo/chromedriver')
url = 'http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679'

driver.get(url)
driver.add_cookie({"name": "bbs_ordr", "value":"60067"})
driver.add_cookie({"name": "bbs_no", "value":"63"})

print(driver.get_cookies())
time.sleep(1)
driver.close()
# from seleniumjs import SessionStorage
#
# driver = webdriver.Chrome('/Users/osangjin/Desktop/dev/Algo/chromedriver')
# url = 'http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679'
#
# driver.get(url)
# sessionStorage = SessionStorage(driver)
# sessionStorage.setItem('key', 'value')
# print(sessionStorage.length)
