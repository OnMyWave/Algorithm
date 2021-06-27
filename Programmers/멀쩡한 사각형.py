import math

def solution(w,h):
    if w == 1 or h == 1:
        return 0
    elif w == h:
        return w*h - w
    else:
        answer = 0
        for i in range(1,w+1):
            answer += math.ceil(h*i/w)-math.floor(h*(i-1)/w)
        return w*h - answer