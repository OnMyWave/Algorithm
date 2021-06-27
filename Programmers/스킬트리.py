from collections import deque

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        available = True
        queue = deque([i for i in skill])
        
        for s in skill_tree:
            if s in queue:
                if queue.popleft() != s:
                    available = False
                    break
        if available :
            answer += 1
    return answer