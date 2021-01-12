from itertools import combinations

a=[2,3,4,5,6,7]
for i in range(2,50):
    b = list(combinations(a, i))
    print(b)