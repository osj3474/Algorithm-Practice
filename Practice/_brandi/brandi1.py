costs = list(map(int, input().split()))
flower_str = input()

# costs = [0,0,0]
costs_dic = {}
costs_dic['R'] = costs[0]
costs_dic['G'] = costs[1]
costs_dic['B'] = costs[2]

# flower_str = 'RRGGB'

flower_cnt = {'R':0, 'G':0, 'B':0}

length = len(flower_str)

def makeFlowerList():
    flower_lst = [0]*length
    i = 0
    for flower in flower_str:
        flower_lst[i] = flower
        flower_cnt[flower] += 1
        i += 1
    return flower_lst


# sub_lst 중에 원하는 flower가 있으면 인덱스를 반환 (없으면 None 반환)
def findReplace(sub_lst, length, flower):
    if flower_cnt[flower] != 0:
        for i in range(length):
            if sub_lst[i] == flower:
                flower_cnt[flower] -= 1
                return i
    return None

batch_lst = ['RGB','RBG','GRB','GBR','BRG','BGR']
total_cost = [0] * len(batch_lst)
total_move = [0] * len(batch_lst)
j = 0


flower_origin = makeFlowerList()
flower_lst = flower_origin[:]

for batch in batch_lst:
    for i in range(len(flower_lst)):
        idx = i % 3
        right_flower = batch[idx]
        if flower_lst[i] != right_flower:
            sub_length = length - (i + 1)
            idx = findReplace(flower_lst[i + 1:], sub_length, right_flower)
            if idx != None:
                idx += (i + 1)
                flower_lst[i], flower_lst[idx] = flower_lst[idx], flower_lst[i]
                total_move[j] += 1
            else:
                MIN_key, MIN_value = '', 1000
                for key, value in costs_dic.items():
                    if key != flower_lst[i]:
                        if MIN_value > value:
                            MIN_key, MIN_value = key, value
                flower_lst[i] = MIN_key
                total_cost[j] += costs_dic[MIN_key]
                total_move[j] += 1
    j += 1

answer_lst = list(zip(total_cost, total_move))
answer_lst = sorted(answer_lst, key=lambda x:(x[0], x[1]))
for answer in answer_lst[0]:
    print(answer, end=' ')

#[0, 0, 0, 0, 0, 0]
#[1, 1, 0, 0, 1, 1]
# total_cost, total_move = 0, 0
# batch = 'GBR'
# flower_lst = makeFlowerList()
# for i in range(len(flower_lst)):
#     idx = i % 3
#     right_flower = batch[idx]
#     print(flower_lst[i])
#     if flower_lst[i] != right_flower:
#         sub_length = length - (i + 1)
#         idx = findReplace(flower_lst[i + 1:], sub_length, right_flower)
#         if idx != None:
#             idx += (i + 1)
#             flower_lst[i], flower_lst[idx] = flower_lst[idx], flower_lst[i]
#             total_move[j] += 1
#         else:
#             MIN_key, MIN_value = '', 1000
#             for key, value in costs_dic.items():
#                 if key != flower_lst[i]:
#                     if MIN_value > value:
#                         MIN_key, MIN_value = key, value
#             flower_lst = MIN_key
#             total_cost += costs_dic[MIN_key]
#             total_move += 1



# print(flower_lst)
# print(total_cost)
# print(total_move)
#
