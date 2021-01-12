from bs4 import BeautifulSoup as bs
import requests

url = "http://www.safekorea.go.kr/idsiSFK/neo/sfk/cs/sfc/dis/disasterMsgView.jsp?menuSeq=679"

result = requests.get(url)
soup = bs(result.text, "html.parser")
txt = soup.find("h3", {"class":"level2_title"})
# print(txt)


print(soup.select_one('.content > #content').get_text())
