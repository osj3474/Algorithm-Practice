import re
import pandas as pd

date_lst = list()
file = './input.txt'
with open(file, 'r') as fp:
    while True:
        f = fp.readline()
        if f == '':break
        p = re.compile(".*\"\$date\":\"(\d{4})-(\d{2})-(\d{2}).*")
        date_lst.append(list(re.findall(p, f)[0]))

df = pd.DataFrame(date_lst,columns=['Year', 'Month', 'Day'])
print(df)