# 아무 고민 없이 푸는 법
from itertools import combinations as cm
import math

def solution(numbers, target):
    n = len(numbers)
    answer = 0
    for i in range(n):
        numbers.append(numbers[i]*(-1))

    candidate_set = set(cm(numbers, n))
    for candidate in candidate_set:
        if sum(candidate) == target:
            n_fac = math.factorial(n)
            elements = set(candidate)
            for element in elements:
                n_fac /= math.factorial(candidate.count(element))
            answer += n_fac
    return int(answer)

a, b = [1, 1, 1, 1, 1], 3

print(solution(a, b))
