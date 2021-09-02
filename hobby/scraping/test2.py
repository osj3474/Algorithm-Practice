import asyncio
from functools import partial

# 키워드 정보를 담은 텍스트 파일을 읽어서, 리스트로 반환받는 함수
# input : 파일명
# return : 키워드 리스트
def get_words_from_file(file_name):
    words = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            words.extend(line)
    return words


from bs4 import BeautifulSoup as bs
import requests

# 스크래핑할 url과 selector를 기반으로 뉴스 정보를 반화하는 함수
# input : url정보, selector
# return :
async def get_HTML(url, selector):   # async함수를 코루틴 이라고 부름.
    result = await loop.run_in_executor(None, requests.get, url)
    soup = await loop.run_in_executor(None, bs, result.text, "html.parser")
    news = await loop.run_in_executor(None, soup.select, selector)
    return news


async def test_naver(words):
    NAVER_base_url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=kt+{}&start={}"
    selector = "div.news_wrap.api_ani_send > div > a"

    news_lst = []
    result_dic = {}

    for word in words:
        word = word.strip()
        url = NAVER_base_url.format(word, 1)
        # news = await asyncio.ensure_future(get_HTML(url, selector))

        # for n in news:
        #     news_lst.append((n['title'], n['href']))  # 포털마다 tag명은 다를 수 있음.
        # result_dic[word] = news_lst

        news_lst.append(asyncio.ensure_future(get_HTML(url, selector)))

    # fts = [asyncio.ensure_future(getpage(u)) for u in urls]
    r = await asyncio.gather(*news_lst)
    # print(r)


    # 최종 결과는 result_dic
    # for k, v in result_dic.items():
    #     print("<< kt {} >>".format(k))
    #     print(v, '\n')
    return r

# def test_daum(words):
#     DAUM_base_url = "https://search.daum.net/search?w=news&q=kt+{}&DA=PGD&spacing=0&p={}"
#     selector = "#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a"
#
#     result_dic = {}
#
#     for word in words:
#         url = DAUM_base_url.format(word, 1)
#         result_dic[word] = get_news_info(url, selector)
#
#     # 최종 결과는 result_dic
#     for k, v in result_dic.items():
#         print("<< kt {} >>".format(k))
#         print(v, '\n')


def main():
    words = get_words_from_file("input.txt")
    # result = requests.get("https://search.daum.net/search?w=news&q=kt%20%ED%81%B4%EB%9D%BC%EC%9A%B0%EB%93%9C&DA=PGD&spacing=0&p=2")
    # soup = bs(result.text, "html.parser")
    # news = soup.select("#newsColl > div.cont_divider > ul > li:nth-child(1) > div.wrap_cont > a")[0].get_text()
    # print(news)
    test_naver(words)
#
#
# begin = time()
#
# main()
# end = time()
# print('실행 시간: {0:.3f}초'.format(end - begin))

# url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=kt+기대&start=1"
# selector = "div.news_wrap.api_ani_send > div > a"
#
# print(asyncio.run(get_HTML(url, selector)))
words = get_words_from_file("input.txt")
loop = asyncio.get_event_loop()   # 막히는 구간이 있으면, 넘어가고 계속 작업하도록 loop를 만드는 것이다.
result_lst = loop.run_until_complete(test_naver(words))   # main함수가 끝날 때까지 계속 loop를 돈다.

for result in result_lst:
    for r in result:
        print(r['title'])
# print(r[0][0]['title'])
