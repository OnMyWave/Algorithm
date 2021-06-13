def solution(record):
    answer = []
    user_name = {}
    for r in record:
        list_r = r.split()
        try:
            user_name[list_r[1]] = list_r[2]
        except:
            pass
    for r in record:
        list_r = r.split()
        if list_r[0] == "Enter":
            answer.append(user_name[list_r[1]]+"님이 들어왔습니다.")
        elif list_r[0] == "Leave":
            answer.append(user_name[list_r[1]]+"님이 나갔습니다.")
    
    return answer

