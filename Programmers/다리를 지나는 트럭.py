from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_queue = deque(truck_weights)
    bridge_weight = 0
    crossing_bridge = deque(0 for _ in range(bridge_length))

    while bridge_queue or bridge_weight:

        answer += 1  # 다리 건너는 시간 증가
        bridge_weight -= crossing_bridge.popleft()
        try:
            if bridge_weight + bridge_queue[0] <= weight:
                a = bridge_queue.popleft()
                crossing_bridge.append(a)
                bridge_weight += a
        except:
            pass


        if len(crossing_bridge) != bridge_length:
            crossing_bridge.append(0)

    return answer