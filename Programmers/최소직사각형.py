import sys

def solution(sizes):
    answer = 0
    array = []
    i = -sys.maxsize
    j = -sys.maxsize
    
    for card in sizes:
        array.append(sorted(card))
        
    for card in array:
        if card[0] > i:
            i = card[0]
        if card[1] > j:
            j = card[1]
            
    
    return i*j