cyphertext = [ord(i) for i in input()]
dictionary = []

N = int(input())
for _ in range(N):
    dictionary.append(input())


for j in range(25):
    def transform(x):
        return chr(x+j)
    print(''.join(map(transform,cyphertext)))
    # cyphertext = ''.join(map(transform,cyphertext))
    # for word in dictionary : 
    #     if word in cyphertext:
    #         print(cyphertext)