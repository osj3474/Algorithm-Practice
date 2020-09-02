# CACCCAAAAAC (10+6=16)
# CAAACCCAAAAAAAACAC (12+12=24)

def solution(name):
    alpaDic = {"A":0,"B":1,"C":2,"D":3,"E":4,"F":5,"G":6,"H":7,"I":8,"J":9,"K":10,"L":11,"M":12,"N":13,"Z":1,"Y":2,"X":3,"W":4,"V":5,"U":6,"T":7,"S":8,"R":9,"Q":10,"P":11,"O":12}
    cnt = 0
    length = len(name)

    # 알파벳 변경 파트
    for i in range(len(name)):
        cnt += alpaDic[name[i]]

    # 커서 이동 파트 (4개 중 가장 작은 경우를 선택)
    move_lst = list()
    # 1) 정 방향의 경우
    for i in range(length-1, -1, -1):
        if name[i] != 'A':
            break
    move_lst.append(i)
    # 2) 역 방향의 경우
    for i in range(1, length):
        if name[i] != 'A':
            break
    move_lst.append(length-i)
    # 3) 정->역 방향의 경우
    notA_lst = list()
    for i in range(1, length):
        if name[i] != 'A':
            notA_lst.append(i)
    for i in range(len(notA_lst)-1):
        candidate = notA_lst[i]*2 + (length-notA_lst[i+1])
        move_lst.append(candidate)

    # 4) 역->정 방향의 경우
    for i in range(len(notA_lst)-1, 1, -1):
        candidate = (length - notA_lst[i])*2+notA_lst[i-1]
        move_lst.append(candidate)

    answer = min(move_lst) + cnt
    return answer
    # cf) A가 아닌 것을 찾는 코드가 반복되어 보이지만, A가 아닌 문자의 인덱스를 저장해서 사용하려다가
    # 인덱스 에러를 찾는데 더 걸려서 각각의 케이스에 맞게 각각 구합니다.

def main():
    name = "JEROEN"
    print(solution(name))

main()


