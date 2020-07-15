def solution(bridge_length, weight, truck_weights):
    start = 0  # 다리를 건너고 있는 버스 중 맨 앞 버스의 인덱스
    end = 0    # 대기 중인 버스 중 맨 앞 버스의 인덱스
    time = 0   # 걸린 시간
    length = len(truck_weights)  # 버스 수
    total = 0                    # 다리를 건너고 있는 버스 무게의 총합 
    ck = [0] * length            # 버스가 다리에 진입한, 체크인 시간
    # 마지막 대기 트럭이 들어가고, 리스트를 초과하는 트럭을 포인팅할 때까지
    while end<length:
        # 시간
        time += 1
        # out
        if total+truck_weights[end] > weight:
            # 원래 time-ck[start] == bridge_length일때, out
            # 한 번에 out되는 시간으로 jump
            time += (bridge_length-(time - ck[start]))
            total -= truck_weights[start]
            start +=1
        # in
        if total+truck_weights[end] <= weight:
            ck[end] = time
            total += truck_weights[end]
            end += 1
    # 마지막 트럭이 들어간 시점으로부터 bridge_length만큼 더 걸림
    time += bridge_length
    return time
