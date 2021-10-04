from collections import Counter

# ASCII : 97~121
# 공백, 숫자, 특수문자 버림
def is_valid(s1, s2):
    if 97<=ord(s1)<=122 and 97<=ord(s2)<=122:
        return True
    return False

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    n1 = len(str1)
    n2 = len(str2)

    word1 = []
    word2 = []

    total_set = set()

    for i in range(n1-1):
        if is_valid(str1[i], str1[i+1]):
            temp = str1[i]+str1[i+1]
            word1.append(temp)
            total_set.add(temp)
    for i in range(n2-1):
        if is_valid(str2[i], str2[i+1]):
            temp = str2[i]+str2[i+1]
            word2.append(temp)
            total_set.add(temp)

    cnt1 = dict(Counter(word1))
    cnt2 = dict(Counter(word2))

    inter_cnt, union_cnt = 0,0
    for s in total_set:
        try: c1 = cnt1[s]
        except: c1 = 0

        try: c2 = cnt2[s]
        except: c2 = 0

        # 교집합
        inter_cnt += min(c1, c2)

        # 합집합
        union_cnt += max(c1, c2)

    if union_cnt==0:
        return 65536
    return int(inter_cnt/union_cnt * 65536)


print(solution("FRANCE", "french"))
print(solution("handshake", "shake hands"))
print(solution("aa1+aa2", "AAAA12"))
print(solution("E=M*C^2", "e=m*c^2"))