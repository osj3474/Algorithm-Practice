import copy

# 함수 : (1차원 리스트를 기준으로) rotate를 위한 인덱스를 반환하는 함수
def makeIdx(N):
    idx_lst = list()
    for i in range(N):
        temp_lst = [0] * N
        for j in range(N):
            temp_lst[j] = i + N * (N - j - 1)
        idx_lst += temp_lst
    return idx_lst

# 함수 : 1차원 리스트를 넘겨주면, rotate된 1차원 리스트를 반환하는 함수
def rotate(lst, N, idx_lst):
    i = 0
    new_lst = [0]*N**2
    for idx in idx_lst:
        new_lst[i] = lst[idx]
        i += 1
    return new_lst

# 함수 : 2차원 리스트를 넘겨주면, 1차원 리스트를 반환하는 함수
def makeLongArray(multi_lst, N):
    long_lst = list()
    for lst in multi_lst:
        long_lst += lst
    return long_lst

# 함수 : 1차원 리스트를 넘겨주면, 2차원 리스트를 반환하는 함수
def makeMultiArray(one_lst, N):
    ret = []
    for i in range(0,N**2,N):
        ret.append(one_lst[i:i+N])
    return ret

def makeBoard(M, N, longLock):
    length = N + 2*(M-1)
    board = [[0] * length for _ in range(length)]
    idx = 0
    for i in range(M-1, M-1+N):
        for j in range(M-1, M-1+N):
            board[i][j] = longLock[idx]
            idx += 1
    return board

# 함수 :
def openKey(Llst, Rlst):
    for i in range(len(Llst)):
        if Llst[i] + Rlst[i] != 1:
            return False
    return True

def slidingWindow(M, N):
    if M > N:
        Llst = list(range(M))
        Rlst = list(range(N))
        j = M
        Lret = []
        for i in range(M - 1, -1, -1):
            if j - i > N:
                j -= 1
            Lret.append(Llst[i:j])
        for i in range(N - 1, 0, -1):
            Lret.append(Llst[:i])

        i = 0
        Rret = []
        for j in range(1, N + 1):
            Rret.append(Rlst[i:j])
        for _ in range(M-N):
            Rret.append(Rlst[:])
        for i in range(1, N):
            Rret.append(Rlst[i:])
    elif M < N:
        Llst = list(range(M))
        Rlst = list(range(N))

        j = M
        Lret = []
        for i in range(M - 1, -1, -1):
            Lret.append(Llst[i:j])
        for _ in range(N-M):
            Lret.append(Llst[:])
        for i in range(M - 1, -1, -1):
            Lret.append(Llst[:i])

        i = 0
        Rret = []
        for j in range(1, N + 1):
            if j > M:
                i += 1
            Rret.append(Rlst[i:j])
        for i in range(i + 1, N):
            Rret.append(Rlst[i:])
    else:
        Llst = list(range(M))
        Rlst = list(range(N))

        Lret=[]
        for i in range(N-1, -1, -1):
            Lret.append(Llst[i:])
        for i in range(N-1, 0, -1):
            Lret.append(Llst[:i])

        Rret=[]
        for i in range(1, N+1):
            Rret.append(Rlst[:i])
        for i in range(1, N):
            Rret.append(Rlst[i:])
    return Lret, Rret

def compareKeyLock(key, lock, slidingIdx):
    answer_lst = []
    final = len(lock)**2
    for i_lst, j_lst in slidingIdx:
        i, j = 0, 0
        # lock_temp = makeLongArray(lock, len(lock))
        lock_temp = copy.deepcopy(lock)
        for _ in range(len(i_lst)):
            key_lst = key[i_lst[i]]
            lock_lst = lock[j_lst[j]]
            for p_lst, q_lst in slidingIdx:
                p, q = 0, 0
                for _ in range(len(p_lst)):
                    if key_lst[p_lst[p]] + lock_lst[q_lst[q]] == 1:
                        lock_temp[j_lst[j]][q_lst[q]] = 1
                    p+=1
                    q+=1
                lock_long = makeLongArray(lock, len(lock))
                if sum(lock_long) == final:
                    answer_lst.append(True)
                else:
                    answer_lst.append(False)
            i+=1
            j+=1
    return answer_lst

def solution(key, lock):
    M, N = len(key), len(lock)
    idx_lst = makeIdx(M)
    l, r = slidingWindow(M, N)
    slidingIdx = list(zip(l, r))
    print(slidingIdx)
    answer_lst = []
    for _ in range(4):
        answer_lst+=compareKeyLock(key, lock, slidingIdx)
        key_long = makeLongArray(key, M)
        key_long = rotate(key_long, M, idx_lst)
        key = makeMultiArray(key_long, M)

    if False in answer_lst:
        return False
    return True

def main():
    key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
    lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(solution(key, lock))

# main()
print(slidingWindow(4, 6))
