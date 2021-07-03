from math import sqrt

H, V = map(float,input().split())
c = H / sqrt(H**2+V**2)
x = V * c / (1+c)

a = x / (2*x/sqrt(H**2+x**2))
b = V * (H/sqrt(H**2+x**2)) / (1+c)

print(f"{a:.2f} {b:.2f}")

