T = [ord(i) for i in input()]

for i in range(26):
    def transform(x):
        return chr((x-65+i)%26+65)
    chicken = ''.join(list(map(transform,T[:8])))
    print(chicken)
    if chicken == "CHICKENS":
        print(chicken)
        break


# print(T)


