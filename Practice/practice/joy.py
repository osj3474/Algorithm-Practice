# def solution(number, k, answer=''):
#     length = len(number) - k
#     if length == 0:
#         return answer
#     else:
#         print("length:", length)  # 2
#         print(number)   # 1
#         print(number[:-length + 1])  # number[:-1]
#         Max = max(number[:-length + 1])
#         answer += Max
#         print("answer:", answer)
#         print("")
#         index = number.find(Max)
#         number = number[index+1:]
#         k = k-1
#         return solution(number, k, answer)
#
# def main():
#     number = "4177252841"
#     k = 4
#     print(solution(number, k))
#
# main()
