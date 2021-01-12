from selenium import webdriver
import pandas as pd
import re
import time
import random
from selenium.webdriver.common.by import By

class SessionStorage:
    def __init__(self, driver) :
        self.driver = driver
    def set(self, key, value):
        self.driver.execute_script("window.sessionStorage.setItem(arguments[0], arguments[1]);", key, value)
    def __setitem__(self, key, value):
        self.set(key, value)


driver = webdriver.Chrome('/Users/osangjin/Desktop/dev/Algo/chromedriver')
url = 'http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679'
storage = SessionStorage(driver)

driver.get(url)

CURRENT_ORDER = 30000
PAST_ORDER = 25002

CURRENT_NO = 63
storage["bbs_no"] = CURRENT_NO

data_lst = [0]*(CURRENT_ORDER-PAST_ORDER)
idx = 0
for i in range(PAST_ORDER, CURRENT_ORDER):
    storage["bbs_ordr"] = i
    driver.execute_script("window.location.reload();")
    time.sleep(random.random()+0.3)

    search_result = driver.find_element(By.ID, 'sj')
    txt = search_result.text

    p = re.compile('(\d{4}/\d{2}/\d{2} \d{2}:\d{2}:\d{2})')
    try:
        date = re.findall(p, txt)[0]
    except:
        date = ''

    search_result = driver.find_element(By.ID, 'cn')
    txt = search_result.text

    try:
        content = txt[txt.index('['):txt.index('-송출지역-')]
    except:
        content = ''

    p = re.compile('\-송출지역\-\n(.*)')
    try:
        start_char = re.findall(p, txt)[0]
        broadcast = txt[txt.index(start_char):]
    except:
        broadcast = ''
    data_lst[idx] = [date, content, broadcast]
    idx+=1
    print("{}번째 완료!".format(i))

df = pd.DataFrame(data_lst,columns=['시간', '내용', '송출지역'])
df.to_csv("utf.csv", encoding='utf-8')
df.to_csv("cp.csv", encoding='cp949')
df.to_csv("euc.csv", encoding='euc-kr')

driver.close()