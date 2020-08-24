def match_target(lst, target):
    if not lst:
        if target==0:
            return 1
        else:
            return 0
    return match_target(lst[1:], target-lst[0])+match_target(lst[1:], target+lst[0])

def solution(numbers, target):
    answer = match_target(numbers, target)
    return answer

