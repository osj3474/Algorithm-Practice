import re
import pandas as pd

txt = """[창녕군청] 오늘 15시 35분 대합면 중앙자동차(폐차장) 화재발생. 인근 주민은 안전한 곳으로 대피하고 차량은 우회 바랍니다. (530-1119)

-송출지역-
경상남도 창녕군
"""

content = txt[txt.index('['):txt.index('-송출지역-')]
print(content)
