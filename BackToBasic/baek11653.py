N = int(input())
_max = 10000000

answer = []
i = 2
while i<_max:
    if N%i == 0:
        N//=i
        answer.append(i)

        if N==1: break

        continue
    i += 1

for a in answer:
    print(a)