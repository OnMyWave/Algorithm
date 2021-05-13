
def BinaryToDecimal(binary): 
    decimal = 0 
    for digit in binary: 
        decimal = decimal*2 + int(digit) 
    return str(decimal)

def solution(binary):
    zero_cnt = 0
    num = 0
    s = binary
    while s != '1' :
        if '0' not in s:
            s = str(len(s))
        else:
            new_s = ''
            for b in s:
                if b == '1':
                    new_s += b
                elif b == '0':
                    zero_cnt +=1
                s = str(len(new_s))
        s = bin(int(s))[2:]

        num += 1

        
    answer = [num,zero_cnt]
    return answer

