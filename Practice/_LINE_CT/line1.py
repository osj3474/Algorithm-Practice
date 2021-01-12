from collections import Counter

def solution(boxes):
    length = len(boxes) # 전체 상자의 갯수
    total_lst = list()  # 모든 아이템을 가진 1차원 리스트
    cnt = 0             # 짝이 만들어진 갯수
    for box in boxes:
        total_lst+=box
    total_dic = dict(Counter(total_lst))  # 각 아이템의 갯수를 담은 딕셔너리
    print(total_dic)
    for v in total_dic.values():
        q = v // 2    # q = 2로 나눈 몫
        if q:         # 짝을 만들 수 있는 경우
            cnt += q
        else:         # 몫이 0이라면, 해당 아이템은 1개가 있는 경우
            pass
    return length - cnt

def main():
    boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
    print(solution(boxes))

main()
