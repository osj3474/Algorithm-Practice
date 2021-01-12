import re

txt = "aaaabasdfprgpe"
p = re.compile("a{3,}")
if re.findall(p, txt):
    print(1)