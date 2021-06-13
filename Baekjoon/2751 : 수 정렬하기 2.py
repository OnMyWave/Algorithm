import sys
numbers = []
N = int(input())
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

numbers.sort()
for number in numbers:
    print(number)