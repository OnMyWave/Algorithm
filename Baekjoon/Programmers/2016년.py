from datetime import date

def solution(a, b):
    answer = ''
    given_date = date(2016,1,1)
    input_date = date(2016,a,b)
    diff = input_date - given_date
    daylist = ["FRI","SAT","SUN","MON","TUE","WED","THU"]
    answer = daylist[diff.days%7]
    return answer

print(solution(5,24))