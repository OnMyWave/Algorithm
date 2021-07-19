n,k=map(int,input().split())
cnt = 0
coins=[]

for i in range(n):
  coins.append(int(input()))
coins.sort(reverse=True)

for i in coins:
  if k==0:
      break
  cnt+=k//i
  k%=i
  

print(cnt)