# 키워드 정보를 담은 텍스트 파일을 읽어서, 리스트로 반환받는 함수
# input : 파일명
# return : 키워드 리스트
def get_words_from_file(file_name):
    words = []
    with open(file_name, "r", encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            for i in range(len(line)):
                line[i] = line[i].strip()
            words.extend(line)
    return words


import requests
from bs4 import BeautifulSoup as bs


# 스크래핑할 url과 selector를 기반으로 뉴스 element를 반환하는 함수
# input : url정보, selector
# return : [<a class="news_tit" href=""]
async def fetch(url, selector):   # async함수를 코루틴 이라고 부름.
    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(None, requests.get, url)
    soup = await loop.run_in_executor(None, bs, result.text, "html.parser")
    news = await loop.run_in_executor(None, soup.select, selector)
    return news

def simple_fetch(url, selector):   # async함수를 코루틴 이라고 부름.
    result = requests.get(url)
    soup = bs(result.text, "html.parser")
    news = soup.select(selector)
    return news


import asyncio
# 모든 키워드에 대한 fetch함수 결과를 비동기로 처리하여 리스트로 반환하는 함수
# input : 키워드, base_url, selector, page
# return : fetch의 모든 결과에 대해 리스트
async def get_highlight_target_element(base, base_url, selector, page, words):
    news_lst = []

    for word in words:
        url = base_url.format(base, word, page)
        # print(url, '크로링 중')
        news_lst.append(asyncio.ensure_future(fetch(url, selector)))  # 리스트에 비동기 future 객체를 넣고

    return await asyncio.gather(*news_lst)   # gather하면 비동기 실행하여 결과 반환


async def get_with_not_target_element(base, base_url, selector, page, words1, words2):
    news_lst = []

    for i in words1:
        for j in words2:
            url = base_url.format(base, i, j, page)
            # print(url, '크로링 중')
            news_lst.append(asyncio.ensure_future(fetch(url, selector)))  # 리스트에 비동기 future 객체를 넣고

    return await asyncio.gather(*news_lst)   # gather하면 비동기 실행하여 결과 반환


import re
# output 파일을 읽고 정규표현식 pattern에 맞는 정보를 set에 담아 반환하는 함수
# input : output파일명, pattern
# return : 해당 pattern과 일치하는 정보를 담은 set
def get_past_info(output_filename, pattern):
    past_set = set()
    p = re.compile(pattern)
    with open(output_filename) as f:
        while True:
            line = f.readline()
            if not line: break   # 파일 내용 끝 조건

            result = re.findall(p, line)
            if result:
                t, l = result[0]
                past_set.add((t, l))
    return past_set


from datetime import datetime, timedelta
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