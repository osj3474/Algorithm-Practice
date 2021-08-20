X, Y, W, S = map(int, input().split())
if X < Y: X, Y = Y, X
if (X+Y)%2==0:
    MIN = X*S
else:
    MIN = (X-1)*S+W
print(min(MIN, (X+Y)*W, (X-Y)*W+Y*S))
