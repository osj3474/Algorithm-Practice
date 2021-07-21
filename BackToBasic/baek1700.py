from collections import Counter
from copy import deepcopy

N, K = map(int, input().split())
use_lst = list(map(int, input().split()))

use_dic = Counter(use_lst)
cnt, limit = 0, 0
pocket_set = set()
candidate_lst = list()

for i in range(K):
    # print("{}사용할 차례입니다.".format(use_lst[i]))
    if use_lst[i] in pocket_set:
        # print("{}는 pocket에 있으니 넘어갈게요".format(use_lst[i]))
        now = use_lst[i]
        use_dic[now] -= 1
        if use_dic[now] == 0:
            candidate_lst.append(now)
        # print('[현재 use_dic 상황] {}'.format(use_dic))
        continue
    if limit >= N:
        # print("가방이 가득찼어요")
        out_item = 0
        if candidate_lst:
            out_item = candidate_lst.pop()
            # print("앞으로 사용할 일이 없는 {}는 가방에서 뺍니다.".format(out_item))
        else:
            temp_set = deepcopy(pocket_set)
            temp = 0
            for j in range(i+1, K-1):
                if not temp_set: break
                if use_lst[j] in temp_set:
                    temp = use_lst[j]
                    temp_set.remove(temp)
            if temp:
                out_item = temp
            # print("가방({})에 있는것 중에, 가장 마지막에 사용할건 {}니까 이걸 빼죠".format(pocket_set, out_item))
        if out_item==0:
            out_item = list(pocket_set)[0]
        pocket_set.remove(out_item)
        limit -= 1
        cnt += 1
        # print("----------cnt={}------------".format(cnt))
    now = use_lst[i]
    use_dic[now] -= 1
    if use_dic[now]==0:
        candidate_lst.append(now)
    pocket_set.add(now)
    limit+=1
    # print('[현재 pocket 상황] {}'.format(pocket_set))
    # print('[현재 use_dic 상황] {}'.format(use_dic))

print(cnt)