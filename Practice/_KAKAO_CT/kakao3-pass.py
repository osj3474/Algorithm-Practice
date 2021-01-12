import re

class User:
    def __init__(self, lang, position, career, food, score):
        self.lang = lang
        self.position = position
        self.career = career
        self.food = food
        self.score = score

def solution(info, query):
    answer_lst = [0]*len(query)
    length = len(info)
    user_lst = [0]*length
    score_lst = [0]*length
    i=0
    p = re.compile('[a-z]+|[0-9]+')
    for element in info:
        lang, position, career, food, score = p.findall(element)
        score = int(score)
        user_lst[i] = User(lang, position, career, food, score)
        score_lst[i] = score
        i+=1

    p = re.compile(r'([\w|-]+) and ([\w|-]+) and ([\w|-]+) and ([\w|-]+) (\d+)')
    for k in range(len(query)):
        required_lang, required_position, required_career, required_food, required_score = p.findall(query[k])[0]
        required_score = int(required_score)
        idx_lst = list()
        cnt = 0

        # ck = [False for _ in range(length)]
        # for i in range(length):
        #     if score_lst[i] >= required_score:
        #         ck[i] = True
        #         cnt += 1
        # idx_lst = [i for i in range(length) if ck[i] == True]

        for i in range(length):
            if score_lst[i] >= required_score:
                idx_lst.append(i)
                cnt += 1



        if idx_lst:
            for idx in idx_lst:
                flag = False
                if required_lang == user_lst[idx].lang or required_lang == '-':
                    if required_position == user_lst[idx].position or required_position == '-':
                        if required_career == user_lst[idx].career or required_career == '-':
                            if required_food == user_lst[idx].food or required_food == '-':
                                flag = True
                if flag:
                    pass
                else:
                    cnt -= 1


        answer_lst[k] = cnt


    return answer_lst


def main():
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))

main()