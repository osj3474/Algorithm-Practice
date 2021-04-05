# 대체될 수 있는 단어인지 확인하는 함수
def isReplace(before, after):
    # before, after 모두 단어(string)
    cnt = 0  # 다른 문자 갯수
    for i in range(len(before)):  # 문자 하나씩 비교
        if before[i] != after[i]:
            cnt += 1
            if cnt == 2:
                return False
    return True

# 대체될 수 있는 단어들의 리스트를 반환하는 함수
def findCandidate(begin, words):
    candidate_lst = list()
    if begin in words:   # 이전의 단어는 후보군에서 제외
        words.remove(begin)
    for word in words:   # // O(N)
        if isReplace(begin, word):
            candidate_lst.append(word)
    return candidate_lst

# BFS로 변환될때까지 탐색하고, depth를 반환하는 함수
def BFS(begin, target, words, depth=0):
    candidate_lst = findCandidate(begin, words)
    if candidate_lst:
        if target in candidate_lst:     # 후보군 중에 target단어와 일치하는 케이스가 있다면 종료
            return depth + 1
        for candidate in candidate_lst: # 없는 경우는 각 단어에 대하여 다시 후보군을 찾아 탐색
            depth += 1
            return BFS(candidate, target, words, depth)   # // 인접리스트처럼 후보군에 한해서 BFS이기 때문에, O(N+후보군)
    return 0

def solution(begin, target, words):
    if target not in words:  # 단어꾸러미에 target단어가 아예 없는 경우는 0반환  // O(N)
        return 0
    answer = BFS(begin, target, words)
    return answer

def main():
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))

main()