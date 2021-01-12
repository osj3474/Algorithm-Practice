import requests

url = 'http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679'
response = requests.get(url).text

from lxml.html import fromstring, tostring, HTMLParser
lxml_response = fromstring(response, parser=HTMLParser(encoding="utf-8"))
print(lxml_response)
lxml_table = lxml_response.xpath('//*[@id="cn"]/text()[1]')
print(lxml_table)