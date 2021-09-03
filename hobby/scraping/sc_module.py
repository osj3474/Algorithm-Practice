# 키워드 정보를 담은 텍스트 파일을 읽어서, 리스트로 반환받는 함수
# input : 파일명
# return : 키워드 리스트
def get_words_from_file(file_name):
    words = []
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            for i in range(len(line)):
                line[i] = line[i].strip()
            words.extend(line)
    return words


from bs4 import BeautifulSoup as bs
import requests
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
async def get_target_element(words, base_url, selector, page):
    news_lst = []

    for word in words:
        url = base_url.format(word, page)
        news_lst.append(asyncio.ensure_future(fetch(url, selector)))  # 리스트에 비동기 future 객체를 넣고

    return await asyncio.gather(*news_lst)   # gather하면 비동기 실행하여 결과 반환