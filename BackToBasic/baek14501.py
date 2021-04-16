N = int(input())
task_lst = [list(map(int, input().split())) for _ in range(N)]

def consult(task_lst, value):
    length = len(task_lst)
    for i, task in enumerate(task_lst):
        if (length-i) >= task[0]:
            consult(task_lst[i+1:], value)

    return 1