def solution(participant, completion):
    ck = [False for _ in range(len(participant))]
    par_dic = {}
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] in par_dic:
            new.append(i)
        else:
            new = [i]
        par_dic[participant[i]]=new
    for i in range(len(completion)):
        ck[par_dic.get(completion[i]).pop(0)] = True
    idx = ck.index(False)
    return participant[idx]
