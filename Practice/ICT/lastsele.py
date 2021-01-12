from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/osangjin/Desktop/dev/Algo/chromedriver')
url = 'http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679'
driver.get(url)
import js2py

test =''' function setStorage(key, value){
window.location.href="http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679";
console.log(key, value);}
'''
time.sleep(2)
fun = js2py.eval_js(test)
fun("1","2")