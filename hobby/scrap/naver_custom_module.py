from datetime import datetime, timedelta
from bs4 import BeautifulSoup as bs
import re
# [<a class="news_tit" href=""] 정보들에서 (time, title, link) 찾아서 반환하는 함수
# input : 검색어에 해당하는 뉴스 기사 element 리스트들, 검색어들, 중복제거용 set
# return : ex) {'클라우드': [(time, title, link), ...]}
def get_info_by_element(result_dic, result_lst, words, past_set:set):
    for i in range(len(words)):
        for r in result_lst[i]:
            soup = bs(str(r), "html.parser")
            time_html = soup.select_one("div.info_group")  # 시간 정보가 있는 element에 대한 텍스트

            # todo: 시간 없는 기사에 대해서는 어떻게 할지 논의
            #       시간 정보만 빼고 하는 것도 방법 >> 그렇게 된다면, 시간 계산하는 부분도 try안으로
            try:
                time_before = re.search("(\d+)분 전", time_html.text).groups()[0]  # (00)분 전
                news_time = datetime.now() + timedelta(minutes=-int(time_before))  # 현재시간 - (00)분
                news_time = "{} {}:{}".format(news_time.date(), str(news_time.hour).zfill(2), str(news_time.minute).zfill(2))  # YYYY-MM-DD HH:MM

                report = time_html.select_one("a").text
            except:
                continue

            title = soup.select_one("a.news_tit")['title']
            link = soup.select_one("a.news_tit")['href']

            if (title, link) in past_set:  # 중복 제거, O(1)
                continue
            past_set.add((title, link))
            result_dic[words[i]].add((news_time, report, title, link))

    return result_dic, past_set