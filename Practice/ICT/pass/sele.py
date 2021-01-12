from selenium import webdriver
import time
from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import requests
import re


class SessionStorage:
    def __init__(self, driver) :
        self.driver = driver
    def get(self, key):
        return self.driver.execute_script("return window.sessionStorage.getItem(arguments[0]);", key)
    def set(self, key, value):
        self.driver.execute_script("window.sessionStorage.setItem(arguments[0], arguments[1]);", key, value)
    def remove(self, key):
        self.driver.execute_script("window.sessionStorage.removeItem(arguments[0]);", key)
    def clear(self):
        self.driver.execute_script("window.sessionStorage.clear();")
    def __getitem__(self, key):
        value = self.get(key)
        if value is None:
            raise KeyError(key)
        return value
    def __setitem__(self, key, value):
        self.set(key, value)
    def __contains__(self, key):
        return key in self.keys()
    def __iter__(self):
        return self.items().__iter__()
    def __repr__(self):
        return self.items().__str__()


driver = webdriver.Chrome('/chromedriver')
url = 'http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679'
storage = SessionStorage(driver)

driver.get(url)

storage["bbs_ordr"] = 60067
storage["bbs_no"] = 63
driver.execute_script("window.location.reload();")

search_box = driver.find_element_by_class_name("content")

print(search_box.text)
# driver.close()