from math import ceil
def solution(w,h):
    # a = 0
    # b = min(w,h)
    #
    # for i in range(1,b+1):
    #     if w % i == 0 and h % i == 0:
    #         a = i
    #
    # new_w = w // a
    # new_h = h // a
    tan = h/w

    c= 0
    tile = 0
    for i in range(1,w+1):
        d = tan*i
        tile += ceil(d-c)
        c = d

    return w*h - tile


solution(8,12)