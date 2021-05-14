def solution(s):
    length = len(s) 
    mod_S = length%2
    quotient_S = length//2
    if mod_S :
        return s[quotient_S]
    else:
        return s[quotient_S-1]+s[quotient_S]