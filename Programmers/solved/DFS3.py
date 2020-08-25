def isReplace(before, after):
    cnt = 0
    for i in range(len(before)):
        if before[i] != after[i]:
            cnt += 1
            if cnt == 2:
                return False
    return True

def findCandidate(begin, words):
    candidate_lst = list()
    if begin in words:
        words.remove(begin)
    for word in words:
        if isReplace(begin, word):
            candidate_lst.append(word)
    return candidate_lst

def BFS(begin, target, words, depth=0):
    candidate_lst = findCandidate(begin, words)
    if candidate_lst:
        if target in candidate_lst:
            return depth + 1
        for candidate in candidate_lst:
            depth += 1
            return BFS(candidate, target, words, depth)
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0
    answer = BFS(begin, target, words)
    return answer
