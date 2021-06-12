from collections import deque

def solution(cacheSize, cities):
    cities = [s.lower() for s in cities]
    answer = 0
    cache = deque()
    
    if cacheSize == 0 :
        return len(cities) * 5
    for city in cities:
        if city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1
        else:
            if len(cache) >= cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
    return answer