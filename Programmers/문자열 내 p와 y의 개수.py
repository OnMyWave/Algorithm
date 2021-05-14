def solution(s):
    count_p = s.count("p") + s.count("P")
    count_y = s.count("y") + s.count("Y")
    if count_p == count_y:
        return True
    else: 
        return False