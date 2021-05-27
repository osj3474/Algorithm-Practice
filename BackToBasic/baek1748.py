n = input()
length = len(n)

base = sum([i*9*10**(i-1) for i in range(1, length)])
last = length*(int(n)-10**(length-1)+1)
print(base+last)