from collections import deque

def solution(progresses, speeds):
    answer = []
    queue = deque(progresses)
    speed = deque(speeds)
    while queue:
        count = 0
        try:
            while queue[0] >= 100:
                queue.popleft()
                speed.popleft()
                count += 1
        except:
            pass
        
        if count != 0 :
            answer.append(count)
            
        for i in range(len(queue)):
            queue[i] = queue[i] + speed[i]
        

    return answer