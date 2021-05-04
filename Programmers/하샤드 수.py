def solution(x):
    harshad = 0
    strNumber = str(x)
    length = len(strNumber)
    for i in range(length):
        harshad += int(strNumber[i])
    
    if x % harshad :
        return False
    else:
        return True