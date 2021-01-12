# 출발지를 인자로 넘겨주면, 남은 티켓 중에서 해당 출발지인 티켓을 리스트로 반환하는 함수
def findCandidate(tickets, start):
    candidate_lst = list()
    for ticket in tickets:      # // O(N)
        if ticket[0] == start:  # 원하는 출발지인 경우 해당 티켓 추가
            candidate_lst.append(ticket)
    return candidate_lst

def travel(tickets, start, travel_lst=["ICN"]):
    global answer_lst  # 정답 조합(정답이 여러개 일 수 있기 때문에)
    if not tickets:    # 티켓을 모두 소진했다는 것은 정답이 될 수 있는 경우
        temp = travel_lst[:]      # shallow copy이지만, iterable 객체가 없기 때문에, deep copy와 같음.
        answer_lst.append(temp)   # 복사본을 수정해도 원본에는 타격없음.
        return 1
    candidate_lst = findCandidate(tickets, start)  # 후보군 생성  // O(N)
    if candidate_lst:  # 후보군이 있는 경우만
        for candidate in candidate_lst:      # // O(N)
            last = tickets[:]
            last.remove(candidate)           # ticket 업데이트
            travel_lst.append(candidate[1])  # 여행경로 업데이트
            travel(last, candidate[1], travel_lst)  # 다시 여행 // O(N)
            travel_lst.pop()  # 후보군이 없거나, 티켓 소진시 한칸 이전 상태로 복귀

def solution(tickets):
    global answer_lst      # 정답이 되는 케이스를 모아둘 리스트 생성
    answer_lst = list()
    travel(tickets, "ICN") # 항상 시작은 ICN에서 시작됨.

    answer_lst.sort()      # 알파벳 순서가 앞서는 경로를 반환해야함.
    answer = answer_lst[0]
    return answer

def main():
    tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
    print(solution(tickets))

main()



