from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    while queue:
        cur = queue.popleft()
        cnt = 0
        for p in queue:
            cnt += 1
            if cur > p:
                break
        answer.append(cnt)
    return answer