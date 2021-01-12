def solution(triangle):
    length = len(triangle)
    for i in range(length-1, 0, -1):
        down_lst = triangle[i]
        up_lst = triangle[i-1]
        for j in range(len(up_lst)):
            up_lst[j] += max(down_lst[j], down_lst[j+1])
    return triangle[0][0]

def main():
    triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(triangle))

main()