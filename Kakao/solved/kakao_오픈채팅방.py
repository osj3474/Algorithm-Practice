def solution(record):
    MESG = {"Enter": "님이 들어왔습니다.",
            "Leave": "님이 나갔습니다."}

    nick_info = dict()
    answer = []
    for r in record:
        info = r.split()

        if info[0] == "Leave":
            action, idx = info
            answer.append([idx, MESG[action]])
            continue

        action, idx, name = info
        nick_info[idx] = name

        if info[0] == "Change": continue
        answer.append([idx, MESG[action]])

    for i in range(len(answer)):
        idx, msg = answer[i]
        answer[i] = "".join([nick_info[idx], msg])

    return answer


print(solution(["Enter uid1234 Muzi",
                "Enter uid4567 Prodo",
                "Leave uid1234",
                "Enter uid1234 Prodo",
                "Change uid4567 Ryan"]))