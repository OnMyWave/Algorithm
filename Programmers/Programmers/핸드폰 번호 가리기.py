def solution(phone_number):
    answer = ''
    length = len(phone_number) - 4 
    lastPartOfNumber = phone_number[-4:]
    return "*"*length + lastPartOfNumber