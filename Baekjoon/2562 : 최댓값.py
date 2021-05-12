number = []
for i in range(9):
    number.append(int(input()))
a = max(number)
b = 0
for i in range(len(number)):
    if number[i] == a:
        b= i
print(max(number))
print(b+1)