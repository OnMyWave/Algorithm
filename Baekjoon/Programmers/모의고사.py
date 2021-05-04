

def solution(answers):
    answer = []
    length = len(answers)
    correct_1, correct_2, correct_3 = 0, 0, 0
    num1 = [1, 2, 3, 4, 5]
    num2  = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(length):
        if answers[i] == num1[i % 5]:
            correct_1 += 1
        if answers[i] == num2[i % 8]:
            correct_2 += 1
        if answers[i] == num3[i%10]:
            correct_3 += 1
    correct_score = [correct_1, correct_2, correct_3]
    for person, score in enumerate(correct_score):
        if score == max(correct_score):
            answer.append(person+1)

    return answer

print(solution([1,2,3,4,5]))