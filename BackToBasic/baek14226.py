def BFS(S, current, copy, cnt):
    copyResult = current
    pasteResult = current + copy
    deleteResult = current - 1
    if copyResult==S or pasteResult==S or deleteResult==S:
        return cnt
    BFS(S, copyResult, current, cnt+1)
    BFS(S, pasteResult, copy, cnt + 1)
    BFS(S, deleteResult, copy, cnt + 1)

print(BFS(2, 1, 0, 1))