import asyncio
from time import time

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
def get_HTML(url, selector):
    result = requests.get(url)
    soup = bs(result.text, "html.parser")
    news = soup.select(selector)
    return news


def test_naver(words):
    NAVER_base_url = "https://search.naver.com/search.naver?where=news&sm=tab_pge&query=kt+{}&start={}"
    selector = "div.news_wrap.api_ani_send > div > a"

    news_lst = []
    result_dic = {}

    for word in words:
        word = word.strip()
        url = NAVER_base_url.format(word, 1)
        news = get_HTML(url, selector)

        for n in news:
            news_lst.append((n['title'], n['href']))  # 포털마다 tag명은 다를 수 있음.
        result_dic[word] = news_lst

    # 최종 결과는 result_dic
    for k, v in result_dic.items():
        print("<< kt {} >>".format(k))
        print(v, '\n')

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


begin = time()

main()
end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))
