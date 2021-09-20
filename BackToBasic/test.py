# from collections import defaultdict
#
# N, L, R = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]
# M = len(board[0])
#
# answer = 0
# while True:
#     p = [[0]*M for _ in range(N)]
#     p_dict = defaultdict(set)
#     idx = 1
#     for i in range(N):
#         for j in range(M):
#             for x, y in [(i+1, j), (i, j+1)]:
#                 if x<N and y<M:
#                     d = abs(board[i][j]-board[x][y])
#                     if L<= d <= R:    # 차이가 유효 범위 안이면
#                         print('{},{}={}와 {},{}={}는 차이가 {}니까 들어온거야'.format(i, j, board[i][j], x, y, board[x][y], d))
#                         if p[i][j]==0 and p[x][y]==0: # 선택된 적이 없다면
#                             p[x][y] = p[i][j] = idx
#                             idx += 1
#                         elif p[i][j]==0:
#                             p[i][j] = p[x][y] # 한쪽이 0이 있으면 0이 아닌 것으로, 둘다 0이 아니면, 작은 쪽으로 모두 옮겨야 함.
#                         elif p[x][y]==0:
#                             p[x][y] = p[i][j]
#                         elif p[i][j]==p[x][y]:
#                             pass
#                         else:
#                             M = max(p[i][j], p[x][y])
#                             m = min(p[i][j], p[x][y])
#                             p[x][y] = p[i][j] = m
#                             for tx, ty in p_dict[m]:
#                                 p[tx][ty] = m
#                                 p_dict[m].add((tx, ty))
#                             p_dict[M].clear()
#                         p_dict[p[i][j]].add((i, j))
#                         p_dict[p[i][j]].add((x, y))
#                         print('p_dict[{}]={}'.format(p[i][j], p_dict[p[i][j]]))
#
#     if len(p_dict)==0: break # 종료 조건
#
#     for p in p_dict.items():
#         print(p)
#     print()
#
#     # 대체 값 구하기
#     change = dict()
#     idx = 1
#     for num_lst in p_dict.values():
#         total, cnt = 0, 0
#         for x, y in num_lst:
#             total += board[x][y]
#             cnt += 1
#         change[idx] = total//cnt
#         idx += 1
#
#     # 대체 값 대입하기
#     idx = 1
#     for num_lst in p_dict.values():
#         total, cnt = 0, 0
#         for x, y in num_lst:
#             board[x][y] = change[idx]
#         idx += 1
#
#     for b in board:
#         print(b)
#     print()
#
#     answer += 1
#
# print(answer)

