from itertools import combinations as cb
from itertools import permutations as pm

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

people_lst = [i for i in range(N)]
case_lst = list(cb(people_lst, N//2))
length = len(case_lst)//2

start_lst = case_lst[:length]
link_lst = case_lst[length:]
link_lst.reverse()

def getSum(lst, board):
    total = 0
    temp_lst = list(pm(lst, 2))
    for temp in temp_lst:
        x, y = temp
        total += board[x][y]
    return total



n = N//2
MIN = float('inf')
for i in range(length):
    temp = abs(getSum(start_lst[i], board)-getSum(link_lst[i], board))
    if MIN > temp: MIN = temp

print(MIN)
