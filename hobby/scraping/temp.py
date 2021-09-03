# from bs4 import BeautifulSoup as bs
#
# soup = bs('''<div class="news_area">
#   <div class="news_info">
#     <div class="api_save_group _keep_wrap">
#       <a
#         aria-pressed="false"
#         class="btn_save _keep_trigger"
#         data-url="https://www.businesspost.co.kr/BP?command=article_view&amp;num=248680"
#         href="#"
#         onclick="tCR('a=nws*f.kep&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;u=javascript'); return false;"
#         role="button"
#         ><i class="spnew ico_save">문서 저장하기</i></a
#       >
#       <div class="api_ly_save _keep_save_layer">
#         <a
#           class="spnew_af item item_save _keep_save"
#           data-cr-off="a=nws*f.kepoff&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;u=javascript"
#           data-cr-on="a=nws*f.kepon&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;u=javascript"
#           href="#"
#           role="button"
#           >Keep에 저장</a
#         >
#         <a
#           class="spnew_af item item_quick"
#           href="https://keep.naver.com/"
#           onclick="return goOtherCR(this,'a=nws*f.kephome&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;u='+urlencode(this.href));"
#           target="_blank"
#           >Keep 바로가기</a
#         >
#       </div>
#     </div>
#     <div class="info_group">
#       <a
#         class="info press"
#         href="http://www.businesspost.co.kr/"
#         onclick="return goOtherCR(this, 'a=nws*f.prof&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;g=5374.0000231603&amp;u='+urlencode(this.href));"
#         target="_blank"
#         ><span class="thumb_box"
#           ><img
#             alt=""
#             class="thumb"
#             height="20"
#             onerror="this.src='data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7';this.className='thumb bg_default_press'"
#             src="https://search.pstatic.net/common/?src=http%3A%2F%2Fwww.businesspost.co.kr%2Fimage2014%2Ffavicon_re.ico&amp;type=f54_54&amp;expire=24&amp;refresh=true"
#             width="20" /></span
#         >비즈니스포스트</a
#       ><span class="info">24분 전</span>
#     </div>
#   </div>
#   <a
#     class="news_tit"
#     href="https://www.businesspost.co.kr/BP?command=article_view&amp;num=248680"
#     onclick="return goOtherCR(this, 'a=nws*f.tit&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;g=5374.0000231603&amp;u='+urlencode(this.href));"
#     target="_blank"
#     title="[오늘Who] 이마트 재방문율 높인다, 강희석 구독서비스 활용 확대"
#     >[오늘Who] 이마트 재방문율 높인다, 강희석 구독서비스 활용 확대</a
#   >
#   <div class="news_dsc">
#     <div class="dsc_wrap">
#       <a
#         class="api_txt_lines dsc_txt_wrap"
#         href="https://www.businesspost.co.kr/BP?command=article_view&amp;num=248680"
#         onclick="return goOtherCR(this, 'a=nws*f.body&amp;r=1&amp;i=88155e5a_000000000000000000231603&amp;g=5374.0000231603&amp;u='+urlencode(this.href));"
#         target="_blank"
#         >이마트와 한화생명이 내놓은 구독보험은 매월 3만 원의 보험을 내면 매달
#         이마트에서 쓸 수 있는 <mark>상품권</mark>...
#         <mark>KT</mark>경제경영연구소에 따르면 국내 구독서비스시장 규모는 2016년
#         25조9천억 원에서 2020년 40조1천억 원으로...</a
#       >
#     </div>
#   </div>
# </div>
# ''', 'html.parser')
# tag = soup.div
# # print(type(tag))
# soup = bs(str(tag), "html.parser")
# news_time = soup.select_one("div.info_group > span").text
# title = soup.select_one("a.news_tit")['title']
# link = soup.select_one("a.news_tit")['href']
# print(news_time)
# print(title)
# print(link)

from datetime import datetime, timedelta

time2 = datetime.now()
# print('현재 시간부터 5일 뒤')
# print(time2 + timedelta(days=5)) # 2018-07-28 20:58:59.666626
# print('현재 시간부터 3일 전')
# print(time2 + timedelta(days=-3)) # 2018-07-20 20:58:59.666626
# print('현재 시간부터 1일 뒤의 2시간 전')
news_time = 30
me = datetime.now() + timedelta(minutes=-news_time) #2018-07-24 18:58:59.666626

print("{} {}:{}".format(me.date(), me.hour, me.minute))

