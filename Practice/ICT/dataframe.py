import pandas as pd

cp = pd.read_csv('./data/cp0.csv', encoding="cp949")
euc = pd.read_csv('./data/euc0.csv', encoding="euc-kr")
utf = pd.read_csv('./data/utf0.csv', encoding="utf-8")
for i in range(1, 7):
    temp_cp = pd.read_csv('./data/cp{}.csv'.format(i), encoding="cp949")
    temp_euc = pd.read_csv('./data/euc{}.csv'.format(i), encoding="euc-kr")
    temp_utf = pd.read_csv('./data/utf{}.csv'.format(i), encoding="utf-8")
    cp = pd.concat([cp, temp_cp], ignore_index=True)
    euc = pd.concat([euc, temp_euc], ignore_index=True)
    utf = pd.concat([utf, temp_utf], ignore_index=True)

cp.to_csv('cp949.csv', encoding='cp949')
euc.to_csv('euc-kr.csv', encoding='euc-kr')
utf.to_csv('utf-8.csv', encoding='utf-8')

