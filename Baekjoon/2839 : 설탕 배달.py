N = int(input())
## N = 5*a + 3*b
# a: 5kg의 개수 , b: 3kg의 개수
# min (a+b) , if a and b is not integer : then print(-1)
# integer programming
a = N // 5
while a >= 0:
    b = N - a * 5
    if b%3==0:
        b//=3
        print(a+b)
        break
    if a==0:
        if N%3 ==0:
            print(N%3)
        else:
            print(-1)

    a -= 1