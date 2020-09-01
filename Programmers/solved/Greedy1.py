def solution(n, lost, reserve):
    student_lst = [1] * (n+1)
    for i in reserve:
        student_lst[i] += 1
    for i in lost:
        student_lst[i] -= 1

    for i in range(1, n):
        if student_lst[i] == 0:
            if student_lst[i-1] == 2:
                student_lst[i-1] -= 1
                student_lst[i] += 1
            elif student_lst[i+1] == 2:
                student_lst[i+1] -= 1
                student_lst[i] += 1
    if student_lst[-1] == 0:
        if student_lst[-2] == 2:
            student_lst[-2] -= 1
            student_lst[-1] += 1
    answer = n - student_lst.count(0)
    return answer
