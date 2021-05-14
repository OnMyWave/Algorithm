def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0] - 1
        end = command[1]
        obj = command[2]
        number_list = array[start:end]
        number_list.sort()
        answer.append(number_list[obj-1])
        

    return answer