import re
from bs4 import BeautifulSoup as bs
import requests

def baseCrawl():
    disaster_result = requests.get("http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgList.jsp?emgPage=Y&menuSeq=679")

    disaster_soup = bs(disaster_result.text, "html.parser")

    # p = re.compile('^bbs_tr_\d+_num_td$')
    # num_lst = re.findall(p, txt)

    num = disaster_soup.find_all("table", {"class": "boardList_table"})
    print(num)
    exit(0)
    for n in num:
        n.find()

    table = num.find_all("tbody", {"id":"bbs_tr"})
    print(table)


    # bbs_tr
    # bbs_tr_0_apiData1
    # bbs_tr_0_num_td
    # ellipsis
    # bbs_tr_0_frst_regist_dt_td

    return 1

# txt = 'bbs_tr_0_num_td'
# p = re.compile('^bbs_tr_\d+_num_td$')
# num_lst = re.findall(p, txt)
# print(num_lst)
#

baseCrawl()