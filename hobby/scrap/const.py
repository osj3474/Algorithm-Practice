# input_1 = "C:/Users/ktds/Desktop/scraping/v2/input.txt"
# input_2 = "C:/Users/ktds/Desktop/scraping/v2/input2.txt"
# input_3 = "C:/Users/ktds/Desktop/scraping/v2/input3.txt"
input_1 = "/Users/sangjin/Desktop/osj/kt/hobby/scraping/v2/input.txt"
input_2 = "/Users/sangjin/Desktop/osj/kt/hobby/scraping/v2/input2.txt"
input_3 = "/Users/sangjin/Desktop/osj/kt/hobby/scraping/v2/input3.txt"

# output_file_name = "C:/Users/ktds/Desktop/scraping/v2/output/bad_news-{}.txt"
# past_file_name = "C:/Users/ktds/Desktop/scraping/v2/output/past_news-{}.txt"
output_file_name = "/Users/sangjin/Desktop/osj/kt/hobby/scraping/v2/output/bad_news.txt"
past_file_name = "/Users/sangjin/Desktop/osj/kt/hobby/scraping/v2/output/past_news.txt"

BATCH_TIME = 30

NAVER_URL_highlight = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={}+{}&oquery=kt&tqi=hgb8pwprvxZssOWHicdssssstZw-523363&nso=so%3Ar%2Cp%3Aall&mynews=0&office_section_code=0&office_type=0&pd=7&photo=0&sort=0&start={}"
NAVER_URL_with_not = "https://search.naver.com/search.naver?where=news&query={}+{} %26 {}&sm=tab_opt&sort=0&photo=0&field=0&pd=7&ds=&de=&docid=&related=0&mynews=0&office_type=0&office_section_code=0&news_office_checked=&nso=so%3Ar%2Cp%3Aall&is_sug_officeid=0&start={}"

NAVER_selector = "div.news_wrap.api_ani_send > div.news_area"

regex_file = "\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{1,2} (.+) (http.+)"
regex_past = "\| .+ \| (.+) \| (.+)"

