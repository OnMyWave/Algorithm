def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0 :
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1 :
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
                
    return max(triangle[-1])

if __name__ == "__main__":
    n = int(input())
    triangle = []
    for i in range(n):
        triangle.append(list(map(int,input().split())))
    print(solution(triangle))