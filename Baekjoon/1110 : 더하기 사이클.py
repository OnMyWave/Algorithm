number = input()
a = number
count = 0
while True:
    if len(number) == 1:
        number = '0'+number
    newNumber = str(int(number[0]) + int(number[-1]))
    newNumber = number[-1]+newNumber[-1]
    number = newNumber
    count+=1
    if int(newNumber) ==int(a) :
        break

print(count)