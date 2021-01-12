N = int(input())
MAX = 220 - N

def checkTrain(heart):
    status = heart/MAX * 100
    ret = 0
    if status >= 90:
        ret = 0
    elif status >= 80:
        ret = 1
    elif status >= 75:
        ret = 2
    elif status >= 68:
        ret = 3
    elif status >= 60:
        ret = 4
    else:
        ret = 5
    return ret

answers = [0] * 6
while 1:
    try:
        heart = int(input())
        idx = checkTrain(heart)
        answers[idx] += 1
    except:
        break

for answer in answers:
    print(answer, end=' ')