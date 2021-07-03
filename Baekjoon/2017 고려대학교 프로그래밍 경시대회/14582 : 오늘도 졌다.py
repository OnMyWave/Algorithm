woolim = list(map(int,input().split()))
startlink = list(map(int,input().split()))

w_over_s = "No"
woolim_cnt = 0
startlink_cnt = 0
for i in range(9):
    woolim_cnt += woolim[i]
    if woolim_cnt > startlink_cnt:
        w_over_s = "Yes"
        break
    startlink_cnt += startlink[i]
print(w_over_s)