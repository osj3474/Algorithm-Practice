input_lst = []
while(1):
    element = int(input())
    if element == 0:
        break
    input_lst.append(element)

N = 123456

ck = [False for _ in range(2*N+1)]
prime_lst = [False for _ in range(2*N+1)]

for i in range(2, len(ck)):
    if ck[i]:
        continue
    prime_lst[i] = True
    for j in range(i*2, len(ck), i):
        ck[j] = True

for i in range(len(input_lst)):
    print(sum(prime_lst[input_lst[i]+1:input_lst[i]*2+1]))
