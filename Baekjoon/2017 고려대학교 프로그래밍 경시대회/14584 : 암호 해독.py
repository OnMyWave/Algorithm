cyphertext = [ord(i) for i in input()]
dictionary = []

N = int(input())
for _ in range(N):
    dictionary.append(input())

for j in range(26):
    def transform(x):
        return chr((x-97+j)%26+97)
    text = ''.join(map(transform,cyphertext))
    for word in dictionary : 
        if word in text:
            print(text)
            break