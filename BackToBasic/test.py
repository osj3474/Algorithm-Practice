import re

def operator(infix_str):
    while re.findall('\*|\/', infix_str):
        infix_str = re.sub('(\d+)\*(\d+)', lambda x:str(int(x.groups()[0])*int(x.groups()[1])), infix_str)
        infix_str = re.sub('(\d+)\/(\d+)', lambda x:str(int(x.groups()[0])/int(x.groups()[1])), infix_str)
    while re.findall('\+|\-', infix_str):
        infix_str = re.sub('(\d+)\+(\d+)', lambda x: str(int(x.groups()[0]) + int(x.groups()[1])), infix_str)
        infix_str = re.sub('(\d+)\-(\d+)', lambda x: str(int(x.groups()[0]) - int(x.groups()[1])), infix_str)
    return infix_str

a = "(()[[]])([])"

a = re.sub('\(\)', '2', a)
a = re.sub('\[\]', '3', a)
a = re.sub('\(|\[', '+(', a)
a = re.sub('\)', ')*2', a)
a = re.sub('\]', ')*3', a)

a = re.sub('\((\d+)\)', lambda x:x.groups()[0], a)
infix_str = a[1:]


num_lst = re.findall('\((.+)\)', infix_str)


while 1:
    num_lst = re.findall('\((.+)\)', infix_str)
    if num_lst:
        result = operator(num_lst[0])
        infix_str = re.sub('\(.+\)', result, infix_str, 1)
    else:
        result = operator(infix_str)
        break


print(result)

# a = '11*2'
# print(re.sub('(\d+)\*(\d+)', lambda x:x.groups()[0]+'/'+x.groups()[1], a))


