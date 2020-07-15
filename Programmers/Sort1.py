def solution(array, commands):
    length = len(commands)
    ret = [0 for _ in range(length)]
    for idx in range(length):
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]

        extract = sorted(array[i-1:j])
        ret[idx] = extract[k-1]
    return ret
