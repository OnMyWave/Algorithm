from collections import defaultdict

def solution(begin, target, words):
    answer = []

    # 한 글자만 차이나는 단어끼리 map 만들기
    length = len(words[0])
    maps = defaultdict(list)
    for i in [begin]+words:
        for j in words:
            cnt = 0
            for k in range(length):
                if i[k] == j[k]:
                    cnt += 1
            if cnt == length-1:
                maps[i].append(j)

    def dfs(word,cnt=0,visited=[]):
        if word == target:
            answer.append(cnt)
        else:
            visited.append(word)
            for i in maps[word]:
                if i not in visited:
                    dfs(i,cnt+1,visited)

    dfs(begin)
    
    if len(answer) :
        return min(answer)
    else:
        return 0

