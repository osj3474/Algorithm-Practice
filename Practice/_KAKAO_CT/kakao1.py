def recommend(new_id_lst):
    answer_lst=list()
    while 1:
        # 1단계
        for i in range(len(new_id_lst)):
            asc = ord(new_id_lst[i])
            if asc >= 65 and asc <= 90:
                asc += 32
                new_id_lst[i] = chr(asc)

        # 2단계 97~122, -(45), _(95), .(46) 만된다.
        for i in range(len(new_id_lst)):
            asc = ord(new_id_lst[i])
            if (asc >= 97 and asc <= 122) or asc == 45 or asc == 95 or asc == 46 or (asc >= 48 and asc <= 57):
                pass
            else:
                new_id_lst[i] = ''
        new_id = "".join(new_id_lst)
        new_id_lst = list(new_id)
        # print("2:", new_id)


        # 3단계
        for i in range(len(new_id_lst) - 1):
            if new_id_lst[i] == '.':
                if new_id_lst[i + 1] == '.':
                    new_id_lst[i] = ''
        new_id = "".join(new_id_lst)
        new_id_lst = list(new_id)
        # print("3:", new_id)

        # 4단계
        if new_id_lst:
            if new_id_lst[0] == '.':
                new_id_lst[0] = ''
        if new_id_lst:
            if new_id_lst[-1] == '.':
                new_id_lst[-1] = ''
        new_id = "".join(new_id_lst)
        new_id_lst = list(new_id)
        # print("4:", new_id)

        # 5단계
        if new_id_lst:
            pass
        else:
            new_id_lst.append('a')
        # print("5:", new_id)

        # 6단계
        if len(new_id_lst) >= 16:
            new_id_lst = new_id_lst[:15]

            if new_id_lst[-1] == '.':
                new_id_lst[-1] = ''
        new_id = "".join(new_id_lst)
        new_id_lst = list(new_id)
        # print("6:", new_id)

        # 7단계
        answer_lst+=new_id_lst[:]
        if len(answer_lst) > 2:
            return answer_lst
        else:
            new_id_lst = list(new_id_lst[-1])
    return answer_lst


def solution(new_id):
    new_id_lst = list(new_id)
    new_id_lst = recommend(new_id_lst)
    new_id = "".join(new_id_lst)
    return new_id

def main():
    new_id = "abcdefghijklmn.p"
    print(solution(new_id))

main()

# A~Z : 65~90
# a~z : 97~122

# -_.~!@#$%^&*()=+[{]}:?,<>
# -(45), _(95), .(46) 만된다.

