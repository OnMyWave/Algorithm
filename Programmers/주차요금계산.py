import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    times = defaultdict(int)
    cars = {}
    for record in records:
        r = record.split()
        if r[2] == "IN" : 
            cars[r[1]] = r[0]
        else:
            in_time = cars[r[1]]
            ih,im = map(int,in_time.split(':')) # in_hour, in_minute
            
            out_time = r[0]
            oh,om = map(int,out_time.split(':')) # out_hour, out_minute
            
            diff = (oh-ih)*60 + (om - im)  
            times[r[1]] += diff
            del cars[r[1]]

    # 23:59 영업 종료 
    if len(cars) :
        for k, v in cars.items():
            in_time = cars[k]
            ih,im = map(int,in_time.split(':')) # in_hour, in_minute
            diff = (23-ih)*60 + (59 - im) 
            times[k] += diff
    times = sorted(times.items(), key = lambda x : int(x[0]))      

    for t in times:
        if t[1] <= fees[0]: 
                answer.append(fees[1])
        else:
                answer.append(fees[1] + math.ceil((t[1] - fees[0])/fees[2]) * fees[3])
                
    return answer