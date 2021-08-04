def solution(price, money, count):
    answer = sum([i*price for i in range(1,count+1)])
    if answer > money :
        return answer - money
    else:
        return 0