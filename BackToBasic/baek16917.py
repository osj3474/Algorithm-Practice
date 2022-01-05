a, b, c, x, y = map(int, input().split())
answer = 0

c2 = c * 2
pair = min(x, y)
if (a + b) > c2:
    answer += pair * c2
    if x < y:
        if b > c2:
            answer += (y - pair) * c2
        else:
            answer += (y - pair) * b
    else:
        if a > c2:
            answer += (x - pair) * c2
        else:
            answer += (x - pair) * a
else:
    answer = a * x + b * y

print(answer)