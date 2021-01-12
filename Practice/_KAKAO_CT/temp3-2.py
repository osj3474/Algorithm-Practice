import re
import statistics

class User:
    def __init__(self, id, lang, position, career, food, score):
        self.id = id
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
    score_lst_idx = [0]*length
    i=0
    p = re.compile('[a-z]+|[0-9]+')
    for element in info:
        lang, position, career, food, score = p.findall(element)
        score = int(score)
        user_lst[i] = User(i, lang, position, career, food, score)
        score_lst[i] = score
        score_lst_idx[i] = [score, i]
        i+=1

    MEAN = statistics.median(score_lst)
    score_lst_idx.sort()
    temp_lst = [0]*length
    print(score_lst_idx)
    for i in range(length):
        temp_lst[i]=user_lst[score_lst_idx[i][1]]
    user_lst = temp_lst

    te = length // 2
    p = re.compile(r'([\w|-]+) and ([\w|-]+) and ([\w|-]+) and ([\w|-]+) (\d+)')
    for k in range(len(query)):
        required_lang, required_position, required_career, required_food, required_score = p.findall(query[k])[0]
        required_score = int(required_score)
        idx_lst = list()
        cnt = 0

        if required_score>MEAN:
            for idx in range(te-1, length):
                flag = False
                if required_score <= user_lst[idx].score:
                    if required_lang == user_lst[idx].lang or required_lang == '-':
                        if required_position == user_lst[idx].position or required_position == '-':
                            if required_career == user_lst[idx].career or required_career == '-':
                                if required_food == user_lst[idx].food or required_food == '-':
                                    flag = True
                if flag:
                    cnt += 1
        else:
            for idx in range(te+1):
                flag = False
                if required_score <= user_lst[idx].score:
                    if required_lang == user_lst[idx].lang or required_lang == '-':
                        if required_position == user_lst[idx].position or required_position == '-':
                            if required_career == user_lst[idx].career or required_career == '-':
                                if required_food == user_lst[idx].food or required_food == '-':
                                    flag = True
                if flag:
                    cnt += 1

        answer_lst[k] = cnt


    return answer_lst

def main():
    info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
    print(solution(info, query))

main()



# "- and backend and senior and - 150"
#
# import re
# p = re.compile(r'([\w|-]+) and ([\w|-]+) and ([\w|-]+) and ([\w|-]+) (\d+)')
# query = ["java and backend and junior and pizza 100", \
#          "python and frontend and senior and chicken 200",\
#          "cpp and - and senior and pizza 250",\
#          "- and backend and senior and - 150", \
#          "- and - and - and chicken 100",\
#          "- and - and - and - 150"]
# for element in query:
#     print(p.findall(element)[0])
