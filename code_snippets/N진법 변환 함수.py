def convert(n,jinsu):
    T = "0123456789ABCDEF"
    div, mod = divmod(n,jinsu)
    if div == 0:
        return T[mod]
    else:
        return convert(div,jinsu) + T[mod]