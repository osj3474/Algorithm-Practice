def solution(info, query):
    answer_lst = [0]*len(query)
    length = len(info)
    lang_lst = [0]*length
    position_lst = [0]*length
    career_lst = [0]*length
    food_lst = [0]*length
    score_lst = [0]*length
    i=0
    for element in info:
        lang_lst[i], position_lst[i], career_lst[i], food_lst[i], score_lst[i] = element.split(" ")
        score_lst[i] = int(score_lst[i])
        i+=1

    required_lang_lst = [0] * length
    required_position_lst = [0] * length
    required_career_lst = [0] * length
    required_food_lst = [0] * length
    required_score_lst = [0] * length
    i =0
    for element in query:
        required_lang_lst[i], required_position_lst[i], required_career_lst[i], required_food_lst[i] = element.split(" and ")
        required_food_lst[i], required_score_lst[i] = required_food_lst[i].split(" ")
        required_score_lst[i] = int(required_score_lst[i])
        i+=1

    for k in range(len(query)):
        required_score, required_lang, required_position, required_career, required_food = required_score_lst[k], \
                                                                                           required_lang_lst[k], \
                                                                                           required_position_lst[k], \
                                                                                           required_career_lst[k], \
                                                                                           required_food_lst[k]

        idx_lst = list()
        for i in range(length):
            if score_lst[i] >= required_score:
                idx_lst.append(i)

        for idx in idx_lst:
            if required_lang == lang_lst[idx] or required_lang == '-':
                pass
            else:
                idx_lst.remove(idx)


        for idx in idx_lst:
            if required_position == position_lst[idx] or required_position == '-':
                pass
            else:
                idx_lst.remove(idx)


        for idx in idx_lst:
            if required_career == career_lst[idx] or required_career == '-':
                pass
            else:
                idx_lst.remove(idx)


        for idx in idx_lst:
            if required_food == food_lst[idx] or required_food == '-':
                pass
            else:
                idx_lst.remove(idx)


        answer_lst[k] = len(idx_lst)


    return answer_lst

def main():
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))

main()