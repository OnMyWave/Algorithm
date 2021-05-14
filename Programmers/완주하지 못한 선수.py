def solution(participant, completion):
    participant.sort()
    completion.sort()
    num = len(completion)

    for idx in range(num) :
        if participant[idx] != completion[idx] : return participant[idx]
    return participant[num]