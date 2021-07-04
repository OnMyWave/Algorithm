N = int(input())
S = input()
while True:
    a = S
    S = S.replace("J","")
    S = S.replace("A","")
    S = S.replace("V","")
    if a == S:
        break


if len(S):
    print(S)
else:
    print("nojava")