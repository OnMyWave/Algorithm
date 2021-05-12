N = int(input())
count = 0
for _ in range(N):
    word = input()
    wordList = [i for i in word]
    newWordList = list(set(wordList))
    c = 0
    for i in newWordList:
        if word.rfind(i) != word.find(i):
            a = word.find(i)
            b = word.rfind(i)
            for j in range(a,b):
                if word[j]!= i:
                    c = 1
    count += c

print(N-count)


