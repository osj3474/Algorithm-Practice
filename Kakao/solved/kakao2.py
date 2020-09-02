def splitWord(words):
    countL, countR = 0, 0
    for i in range(len(words)):
        if words[i] == '(':
            countL += 1
        else:
            countR += 1
        if countL == countR:
            break
    if i+1 == len(words):
        u = words
        v = ''
    else:
        u = words[:i + 1]
        v = words[i+1:]
    return u, v

def checkRight(words):
    # 홀수 out
    if len(words) % 2 == 1:
        return False

    # L, R 갯수 안 맞는 경우 out
    countL, countR = 0, 0
    for word in words:
        if word == "(":
            countL += 1
        else:
            countR += 1
    if countL != countR:
        return False

    # 올바르지 않은 경우 out
    cnt = 0
    for word in words:
        if word == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True

def reverseWord(words):
    ret = ''
    for i in range(len(words)):
        if words[i] == '(':
            ret += ')'
        else:
            ret += '('
    return ret

def makeRight(words):
    if words == '':
        return ''
    u, v = splitWord(words)
    if checkRight(u):
        return u+makeRight(v)
    else:
        ret = '('
        ret += makeRight(v)
        ret += ')'
        ret += reverseWord(u[1:-1])
        return ret


def solution(p):
    return makeRight(p)

def main():
    p = "()))((()"
    print(solution(p))

main()
