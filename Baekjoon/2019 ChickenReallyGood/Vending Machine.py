vending_machine = [0,500,800,1000]

buttons = list(map(int,input().split()))
answer = 5000

for button in buttons:
    answer -= vending_machine[button]

print(answer)