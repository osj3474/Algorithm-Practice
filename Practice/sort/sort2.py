# 1. 첫번째 숫자를 기준으로 묶음 별로 정렬한다.
# 2. 해당 묶음 안에서 가장 긴 자릿수를 기준으로 1번의 숫자를 추가한다.
#    (이유는 3과 30을 비교했을 때, 3이 먼저오는 것이 맞는데, 이 때,
#     첫번째 숫자인 30의 일의 자릿수가 3보다 커야지 앞으로 갈 수 있기 때문이다.생각해보라.)
# 3. 정렬한다. 끝

from collections import defaultdict

def addSelf(before, n):
    n -= len(before)
    after = before + '{}'.format(before[0])*n
    return [after, before]

def sortSubgroup(numbers):
    MAX = int(sorted(numbers, key=lambda x: len(x))[0])
    MAX = [MAX for _ in range(len(numbers))]
    new_numbers = list(map(addSelf, numbers, MAX))
    new_numbers.sort(reverse=True)
    for i in range(len(new_numbers)):
        numbers[i] = new_numbers[i][1]
    return numbers

def solution(numbers):
    numbers_str_lst = list(map(str, numbers))
    numbers_group_dic = defaultdict(list)
    for number_str in numbers_str_lst:
        numbers_group_dic[number_str[0]].append(number_str)

    ret = []
    for key, numbers_lst in numbers_group_dic.items():
        ret.append([int(key), sortSubgroup(numbers_lst)])
    ret = sorted(ret, key=lambda x:x[0], reverse=True)
    answer = ''
    for group in ret:
        for number in group[1]:
            answer += number
    return str(answer)

def main():
    numbers = [3, 30, 34, 5, 9]
    print(solution(numbers))

main()



