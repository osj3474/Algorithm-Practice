import asyncio
import shutil
from collections import defaultdict

import const
from sc_module import get_highlight_target_element
from sc_module import get_info_by_element
from sc_module import get_past_info
from sc_module import get_with_not_target_element
from sc_module import get_words_from_file

from naver_custom_module import get_info_by_element


# 네이버 뉴스를 스크래핑하는 함수
def scrap():
    # ======================================== 세팅 ======================================== #
    base_word = ['kt']  # 기본 조합어

    # 과거 뉴스 저장
    past_set = set()

    shutil.copyfile(const.output_file_name, const.past_file_name)  # bad_news >> past_news
    past_info = get_past_info(const.output_file_name, const.regex_past)

    for info in past_info:
        past_set.add(info)

    words_1 = get_words_from_file(const.input_1)    # 하이라이트 검색어
    words_2 = get_words_from_file(const.input_2)    # 하이라이트 아닌 검색어
    words_3 = get_words_from_file(const.input_3)    # 부정 키워드

    url_lst = []
    url_lst.append(const.NAVER_URL_highlight)  # 1. 하이라이트 키워드            (word_1)
    url_lst.append(const.NAVER_URL_with_not)   # 2. 하이라이트 아닌 검색어 + 부정  (word_2 & word_3)

    selector = const.NAVER_selector


    # ======================================== 스크래핑 ======================================== #
    result_dic = defaultdict(set)

    for q in range(len(base_word)):
        for url in url_lst:
            loop = asyncio.get_event_loop()

            # todo: pagination 처리 로직 추가 (2페이지 이상에 대하여)
            # 1. 하이라이트 키워드
            if url == const.NAVER_URL_highlight:
                result_lst = loop.run_until_complete(get_highlight_target_element(base_word[q], url, selector, 1, words_1))   # main함수가 끝날 때까지 계속 loop를 돈다.
                result_dic, past_set = get_info_by_element(result_dic, result_lst, words_1, past_set)


            # 2. 하이라이트 아닌 검색어 + 부정
            elif url == const.NAVER_URL_with_not:
                result_lst = loop.run_until_complete(get_with_not_target_element(base_word[q], url, selector, 1, words_2, words_3))
                result_dic, past_set = get_info_by_element(result_dic, result_lst, words_2, past_set)


    # ======================================== 파일로 저장 ======================================== #
    file_name = const.output_file_name.format("kt")
    f = open(str(file_name), 'w', encoding='UTF-8')

    idx = 1
    for k, v in result_dic.items():
        if not v: continue

        for news_time, report, title, link in v:
            output = '('+str(idx)+') '+' | '.join(map(str, [news_time, report, title, link]))

            print(output)
            f.write(output)
            print()
            f.write('\n\n')

            idx += 1
    f.close()


from time import time

begin = time()

scrap()

end = time()
print('실행 시간: {0:.3f}초'.format(end - begin))