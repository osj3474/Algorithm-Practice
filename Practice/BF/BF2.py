# import math
#
# # yellow블럭으로 만들 수 있는 경우의 수를 나열하고, 그것을 brown블럭이 둘러싼다고 했을 때,
# # brown 갯수와 맞으면 정답 처리
# def solution(brown, yellow):
#     perfect = math.sqrt(brown+yellow)
#     answer = 0
#     if int(perfect) == perfect:
#         answer = [perfect, perfect]
#     # row가 1인 경우
#     # 1) yellow가 홀 수인 경우
#     # 2) row가 1이라고 가정했을 때, brown 갯수가 일치하는 경우
#     if (brown == (yellow+1)*2+4) or yellow%2:
#         answer = [yellow+2, 3]
#     # row가 될 수 있는 최대치
#     row = int(math.sqrt(yellow))
#     for r in range(2, row+1):
#         c = yellow // r
#         brown_cnt = (r+c)*2+4
#         if brown == brown_cnt:
#             answer = [c+2, r+2]
#             break
#     return answer
#
# def main():
#     brown = 8
#     yellow = 1
#     print(solution(brown, yellow))
#
# main()


print(divmod(10,3))