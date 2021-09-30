from sc_module import get_words_from_file
from sc_module import get_target_element

import asyncio

from bs4 import BeautifulSoup as bs

import re
from datetime import datetime, timedelta

# 네이버 뉴스를 스크래핑하는 함수
def test_naver():
    words = get_words_from_file("input.txt")

    NAVER_base_url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=kt+{}&oquery=kt&tqi=hgb8pwprvxZssOWHicdssssstZw-523363&nso=so%3Ar%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=7&photo=0&sort=0&start={}"
    selector = "div.news_wrap.api_ani_send > div.news_area"

    loop = asyncio.get_event_loop()  # 막히는 구간이 있으면, 넘어가고 계속 작업하도록 loop를 만드는 것이다.
    result_lst = loop.run_until_complete(get_target_element(words, NAVER_base_url, selector, 1))   # main함수가 끝날 때까지 계속 loop를 돈다.

    result_dic = {}

    for i in range(len(words)):
        temp = []
        for r in result_lst[i]:
            soup = bs(str(r), "html.parser")
            time_html = soup.select_one("div.info_group").text                  # 시간 정보가 있는 element에 대한 텍스트
            time_before = re.search("(\d+)분 전", time_html).groups()[0]         # (00)분 전

            news_time = datetime.now() + timedelta(minutes=-int(time_before))   # 현재시간 - (00)분
            news_time = "{} {}:{}".format(news_time.date(), news_time.hour, news_time.minute)  # YYYY-MM-DD HH:MM

            title = soup.select_one("a.news_tit")['title']
            link = soup.select_one("a.news_tit")['href']

            temp.append((title, news_time, link))
        result_dic[words[i]] = temp

    for k, v in result_dic.items():
        if not v: continue
        print("< {} >".format(k))
        idx = 1
        for title, news_time, link in v:
            print('({}) {} | {} | {}'.format(idx, news_time, title, link))
            idx += 1
        print()


from time import time

begin = time()

test_naver()

end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))