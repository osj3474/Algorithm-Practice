# [[1, 4], [3, 4], [3, 10]]
# [[1, 1], [2, 2], [1, 2]]

from collections import defaultdict

def solution(v):
    x, y = 0, 0
    x_dict = defaultdict(int)
    y_dict = defaultdict(int)
    for point in v:
        x_dict[point[0]] += 1
        y_dict[point[1]] += 1
    for key, value in x_dict.items():
        if value == 1: x = key
    for key, value in y_dict.items():
        if value == 1: y = key
    return [x, y]


print(solution([[1, 1], [2, 2], [1, 2]]))