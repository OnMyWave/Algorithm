from collections import Counter
N = Counter([i for i in input()])

a = True

for i in N:
    if i not in ['2','0','1','8']:
        print(0)
        a = False
        break

if a == True:
    counter = Counter(N)
    if counter['2']*counter['0']*counter['1']*counter['8'] >= 1:
        if counter['2'] == counter['0'] == counter['1'] == counter['8'] :
            print(8)
        else:
            print(2)
    else:
        print(1)
