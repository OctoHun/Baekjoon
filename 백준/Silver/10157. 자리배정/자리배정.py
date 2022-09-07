c, r = map(int, input().split())
k = int(input())
si = r
sj = 0
num = 1
arr = [[0] * c for _ in range(r)]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
flag = 0
ans = 1
i = 0
if c * r < k:
    ans = 0
    flag = 1
while flag == 0:
        if 0 <= si+di[i] < r and 0 <= sj+dj[i] < c and arr[si+di[i]][sj+dj[i]] == 0:
            si += di[i]
            sj += dj[i]
            arr[si][sj] = num
            if num == k:
                a, b = si, sj
                flag = 1
            num += 1
        else:
            i = (i+1)%4
if ans == 0:
    print(ans)
else:
    print(b+1, r-a)