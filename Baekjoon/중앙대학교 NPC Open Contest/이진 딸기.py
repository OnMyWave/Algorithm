def convert(n,jinsu):
    T = "0123456789ABCDEF"
    div, mod = divmod(n,jinsu)
    if div == 0:
        return T[mod]
    else:
        return convert(div,jinsu) + T[mod]


T = int(input())

for _ in range(T):
    num = (int(input())-1)%28+1
    if num >= 15 :
        num = 30 - num
    bit = convert(num,2)
    while len(bit) != 4:
        bit = "0" + bit
    answer = ''.join(["V" if i == "0" else "딸기" for i in bit])
    print(answer)