from collections import defaultdict

dic = defaultdict(int)
for a in range(21):
    for b in range(21):
        for c in range(21):
            if a <= 0 or b <= 0 or c <= 0 :
                dic[(a,b,c)] =  1
            elif a < b and b < c :
                dic[(a,b,c)] = dic[(a, b, c-1)] + dic[(a, b-1, c-1)] - dic[(a, b-1, c)]
            else:
                dic[(a,b,c)] = dic[(a-1, b, c)] + dic[(a-1, b-1, c)] + dic[(a-1, b, c-1)] - dic[(a-1, b-1, c-1)]

    
while True:
    a,b,c = map(int,input().split())
    if (a,b,c) == (-1,-1,-1):
        break 
    else:
        if a<= 0 or b<= 0 or c <= 0:
            print(f"w({a}, {b}, {c}) = {1}")
        elif a > 20 or b > 20 or c > 20 : 
            print(f"w({a}, {b}, {c}) = {dic[(20,20,20)]}")
        else:
            print(f"w({a}, {b}, {c}) = {dic[(a,b,c)]}")