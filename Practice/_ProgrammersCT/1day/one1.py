def solution(numbers):
    answer = set()
    length = len(numbers)
    for i in range(length-1):
        for j in range(i+1, length):
            answer.add(numbers[i] + numbers[j])
    return sorted(list(answer))

def main():
    numbers = [5,0,2,7]
    print(solution(numbers))

main()