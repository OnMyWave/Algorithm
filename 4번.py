def solution(n):
  arr = []
  a, b, c = 2, 0, 1
  for i in range(n):
    if i != 0 and i % 4 == 0:
      b = a * (a+1) * (a+2)
      arr.append(b)
      a += 1
    else:
      arr.append(c * (c+1))
      c += 1
  print(arr)
  return arr[n-1]
