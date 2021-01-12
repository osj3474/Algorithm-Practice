# 1번
# 문제 : numbers라는 배열이 주어지고, 그 배열 안에 원소 중 과반수가 넘는 원소를 찾아서 리턴, 없으면 -1 리턴
from collections import defaultdict

# 일단 먼저 정렬을 하고 다시 하나씩 본다면, nlogn + n/2가 된다.
# 반면 아래처럼 하면 n만에 끝난다.
def solution(numbers):
    half = len(numbers)//2+1    # 과반수, 가령, 4라면 3이, 5라면, 3이된다.
    num_dic = defaultdict(int)  # 나온 숫자의 횟수를 세기 위한 딕셔너리
    MAX = 0                     # 가장 많이 나온 숫자의 횟수
    answer = 0
    for num in numbers:         # 전부 다 돌면서
        num_dic[num]+=1         # 몇개인지 세아리고
        if MAX < num_dic[num]:  # MAX 계속 업뎃
            MAX = num_dic[num]
            answer = num        # MAX를 찍는 숫자 자체를 answer에 넣음
    if MAX >= half:             # for문 다 돌고는 마지막에 half기준으로 answer할지, -1할지
        return answer
    else:
        return -1

def main():
    numbers = [6,6,6,2,2,2]
    print(solution(numbers))

main()