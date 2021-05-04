def solution(s):
    answer = True
    try:
        a = int(s)
        if (len(str(a)) == 4 or len(str(a)) == 6 ) :
            return answer
    except:
        return False