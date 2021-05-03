def solution(numbers, hand):
    answer = ''
    lefthand = [0, 3]
    righthand = [2, 3]
    keypad = [[1, 4, 7], [2, 5, 8, 0], [3, 6, 9]]
    for number in numbers:
        if number in keypad[0]:
            answer += "L"
            lefthand = [0,keypad[0].index(number)]
        elif number in keypad[2]:
            answer += "R"
            righthand = [0,keypad[2].index(number)]
        else:
            indexN = keypad[1].index(number)
            uclL = abs(lefthand[0]-1) +abs(lefthand[1]-indexN)
            uclR = abs(righthand[0]-1) +abs(righthand[1]-indexN)
            if uclR == uclL:
                if hand == "left":
                    answer += "L"
                    lefthand = [1, indexN]
                else:
                    answer += "R"
                    righthand = [1, indexN]
            elif uclR < uclL:
                answer += "R"
                righthand = [1, indexN]
            elif uclR > uclL:
                answer += "L"
                lefthand = [1, indexN]

    return answer