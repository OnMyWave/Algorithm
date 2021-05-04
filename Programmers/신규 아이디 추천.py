
def solution(new_id):
    answer = ''
    
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    char_list = [chr(i) for i in range(97,123)] # 소문자
    char_list = char_list + ['-','_','.','1','2','3','4','5','6','7','8','9','0']  # 숫자 추가
    for char in new_id :
        if char not in char_list:
            new_id = new_id.replace(char,"") 
    
    # 3단계
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    
    # 4단계
    try:
        if new_id[0] == '.' :
            new_id = new_id[1:]
        if new_id[-1] == '.':
            new_id = new_id[:-1]    
    except:
        pass
        
    # 5단계
    if new_id == "":
        new_id = "a"
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    
    # 7단계
    if len(new_id)<= 2 :
        while len(new_id)<3:
            new_id += new_id[-1]
            
    
    return new_id