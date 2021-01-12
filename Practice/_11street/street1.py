import re
def solution(S):
    p = re.compile("a{3,}")
    ck = re.findall(p, S)
    if ck:
        return -1
    S_lst = list(S)
    a_cnt = S_lst.count("a")
    p = re.compile("[^a]")
    not_a_cnt = len(re.findall(p, S))

    total = (not_a_cnt+1)*2
    answer = total - a_cnt
    return answer


def main():
    S = "aasdfasadfasdf"
    print(solution(S))

main()
