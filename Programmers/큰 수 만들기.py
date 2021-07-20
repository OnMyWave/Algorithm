def solution(number, k):
    answer = ''
    cnt = 0 
    idx_list = []
    while cnt < k:
        for i in range(len(number)-1):
            if number[i] < number[i+1]:
                if i == 0 :
                    number = number[1:]
                else:
                    number = number[:i] + number[i+1:]
                break
        cnt += 1
    return number


def solution2(number, k):
    number = list(map(int,number))
    cnt = 0
    while cnt < k:
        max_idx = number.index(max(number))
        min_num = max(number)
        for i in range(max_idx):
            min_num = min(number[i],min_num)
        number.remove(min_num)
        cnt += 1
    return ''.join(list(map(str,number)))

print(solution2("1924", 2))

def solution3(number, k):
    length = len(number)
    if length == 1:
        return number[0]
    else:
        while k:
            for i in range(length-1):
                if number[i] < number[i+1]:
                    number = number[:i] + number[i+1:]
                    break
            length -= 1
            k -= 1
        return number