def solution(numbers):
    answer = []
    length = len(numbers)
    for i in range(length) :
        for j in range(i+1,length):
            if numbers[i] + numbers[j] not in answer:
                answer.append(numbers[i] + numbers[j])
    answer.sort()
    return answer
