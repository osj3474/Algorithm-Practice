import re
import datetime as dt

customers=["10/01 23:20:25 30", "10/01 23:25:50 26"]

length = len(customers)
month_lst = [0]*length
date_lst = [0]*length
hour_lst = [0]*length
minute_lst = [0]*length
second_lst = [0]*length
work_lst = [0]*length

# p = re.compile("(\d{2})\/(\d{2}) (\d{2})\:(\d{2})\:(\d{2}) (\d{2})")
# for i in range(length):
#     month_lst[i], date_lst[i], hour_lst[i], minute_lst[i], second_lst[i], work_lst[i] = map(int,list(re.findall(p, customers[i])[0]))
#     print(dt.datetime(2019, month_lst[i], date_lst[i], hour_lst[i], minute_lst[i], second_lst[i])+dt.timedelta(minutes=work_lst[i]))

lst = [0]*3
lst[1]=dt.datetime(2019, 10,1,12,00,30)
lst[0]=dt.datetime(2019, 10,1,13,00,30)
lst[2]=dt.datetime(2019, 10,1,14,00,30)


response = [0]*3
MIN = min(lst)
MIN_idx = lst.index(MIN)
response[MIN_idx] += 1
a = [1,2,3,3,4]
# print(a.index(3))

lst = [True, False, False, True]
print(sum(lst))