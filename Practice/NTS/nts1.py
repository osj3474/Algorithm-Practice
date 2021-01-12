MIN = 1
MAX = 366

def solution(flowers):
    answer = 0
    ck = [False for _ in range(MIN, MAX)]
    for flower in flowers:
        for i in range(flower[0], flower[1]):
            ck[i] = True
    answer = sum(ck)
    return answer

def main():
    flowers = [[3, 4],[4, 5], [6, 7], [8, 10]]
    print(solution(flowers))

main()