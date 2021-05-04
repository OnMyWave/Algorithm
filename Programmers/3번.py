def solution(N,sequence):
    answer = 0
    if sequence[0] != 1:
        sequence.insert(0,1)
    length = len(sequence)
    for i in range(0, length - 1):
        answer += min((N + sequence[i + 1] - sequence[i]), abs(sequence[i] - sequence[i + 1]))
    return answer
print(solution(5,[1,2,3,4,5]))
print(solution(5,[3,5,4,1,2]))