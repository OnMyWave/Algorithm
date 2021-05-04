def solution(num):
    count = 0
    
    while num != 1:
        if count < 500:
            count += 1
            if num % 2 :
                num = num*3 +1
            else:
                num /= 2
        else:
            return -1

    return count