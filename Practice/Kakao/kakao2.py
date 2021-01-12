# 함수 : splitWord
# 역할 : '(' 와 ')' 의 갯수가 처음으로 같아지는 지점에서 u, v를 나누는 함수
def splitWord(words):
    countL, countR = 0, 0       # countL = '('의 갯수, countR = ')'의 갯수
    for i in range(len(words)): # 문자를 처음부터 끝까지 반복문
        if words[i] == '(':
            countL += 1         # '('인 경우, countL 증가
        else:
            countR += 1         # ')'인 경우, countR 증가
        if countL == countR:    # 매번 갯수를 체크해서 처음으로 같아질 때, 반복문 break
            break
    if i+1 == len(words):       # split 했을 때, v가 ''인지 확인
        u = words
        v = ''
    else:
        u = words[:i + 1]
        v = words[i+1:]
    return u, v

# 함수 : checkRight
# 역할 : 올바른 문자열이라면, True, 그렇지 않으면, False를 반환하는 함수
def checkRight(words):
    # 1) 홀수 out
    if len(words) % 2 == 1:
        return False

    # 2) L, R 갯수 안 맞는 경우 out
    # 3번에서 ((()의 경우를 통과하지 못하여 추가하였음.
    countL, countR = 0, 0
    for word in words:
        if word == "(":
            countL += 1
        else:
            countR += 1
    if countL != countR:
        return False

    # 3) 올바르지 않은 경우 out
    cnt = 0              # '('일 때 +1, ')'일 때 -1을 해줌. (음수가 되면, 올바르지 않은 경우)
    for word in words:
        if word == '(':  # 올바른 문자열은 항상 '('로 시작함.
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True   # 위의 3가지 경우를 모두 통과했다면, True

# 함수 : reverseWord
# 역할 : 문자열의 괄호 방향을 바꿔주는 함수
def reverseWord(words):
    ret = ''
    for i in range(len(words)):
        if words[i] == '(':
            ret += ')'    # '('는 ')'으로.
        else:
            ret += '('    # ')'는 '('으로.
    return ret

# 함수 : makeRight
# 역할 : "올바른 괄호 문자열"로 변환하는 함수
def makeRight(words):
    if words == '':           # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
        return ''
    u, v = splitWord(words)   # 2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다.
    if checkRight(u):         # 3. 문자열 u가 "올바른 괄호 문자열" 이면,
        return u+makeRight(v) #    문자열 v에 대해 1단계부터 다시 수행합니다.
    else:                     # 4. 아니라면 아래 과정을 수행합니다.
        ret = '('
        ret += makeRight(v)
        ret += ')'
        ret += reverseWord(u[1:-1])  # 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        return ret

def solution(p):
    return makeRight(p)

def main():
    p = "()))((()"
    print(solution(p))

main()