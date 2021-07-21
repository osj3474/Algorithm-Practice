def compare(s, t):
    i=0
    length = len(s)
    flag = False
    for p in t:
        if p==s[i]:
            i+=1
            if i >= length:
                flag = True; break
    return flag

try:
    while 1:
        s, t = input().split()
        if compare(s, t): print("Yes")
        else: print("No")
except:
    exit()

