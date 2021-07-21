import re

a = "((3))(2)"
p = re.compile('\(\d\)')
print(re.findall(p, a))
print(re.sub(p, lambda x: str(x.group())[1], a))
