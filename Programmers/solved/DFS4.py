def findCandidate(tickets, start):
    candidate_lst = list()
    for ticket in tickets:
        if ticket[0] == start:
            candidate_lst.append(ticket)
    return candidate_lst

def travel(tickets, start, travel_lst=["ICN"]):
    global answer_lst
    if not tickets:
        temp = travel_lst[:]
        answer_lst.append(temp)
    candidate_lst = findCandidate(tickets, start)
    if candidate_lst:
        for candidate in candidate_lst:
            last = tickets[:]
            last.remove(candidate)
            travel_lst.append(candidate[1])
            travel(last, candidate[1], travel_lst)
            travel_lst.pop()

def solution(tickets):
    global answer_lst
    answer_lst = list()
    travel(tickets, "ICN")

    answer_lst.sort()
    answer = answer_lst[0]
    return answer
