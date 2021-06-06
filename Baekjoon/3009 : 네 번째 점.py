from collections import Counter

x_coordinate = []
y_coordinate = []

for _ in range(3):
    x,y = map(int,input().split())
    x_coordinate.append(x)
    y_coordinate.append(y)

x_counter = Counter(x_coordinate).most_common()[1][0]
y_counter = Counter(y_coordinate).most_common()[1][0]

print(x_counter,y_counter)



