m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
q = [0] * (m * n)
first = -1
rear = -1
day = 0
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            rear += 1
            q[rear] = (day, i, j)
while first != rear:
    first += 1
    day, i, j = q[first]
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        ni = di + i
        nj = dj + j
        if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 0:
            arr[ni][nj] = 1
            rear += 1
            q[rear] = (day+1, ni, nj)
for i in range(n):
    for j in range(m):
        if arr[i][j] == 0:
            day = -1
            break
    if day == -1:
        break
print(day)