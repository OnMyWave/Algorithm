import math
from collections import defaultdict

def splitIntoHHMM(hhmm):
    hh, mm = map(int,hhmm.split(':'))
    return hh, mm 
    
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
            ih, im = splitIntoHHMM(in_time)
            
            out_time = r[0]
            oh,om = splitIntoHHMM(out_time)
            
            diff = (oh - ih) * 60 + (om - im)  
            times[r[1]] += diff
            del cars[r[1]]

    # 23:59 영업 종료 
    if len(cars) :
        for k, v in cars.items():
            in_time = cars[k]
            ih, im = splitIntoHHMM(in_time)
            diff = (23 - ih) * 60 + (59 - im) 
            times[k] += diff
    times = sorted(times.items(), key = lambda x : int(x[0]))      

    for t in times:
        if t[1] <= fees[0]: 
                answer.append(fees[1])
        else:
                answer.append(fees[1] + math.ceil((t[1] - fees[0])/fees[2]) * fees[3])
                
    return answer