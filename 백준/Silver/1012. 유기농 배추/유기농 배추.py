def worm():
    global arr, q, visited
    while q:
        i, j = q.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                arr[ni][nj] = 0
                q.append((ni, nj))


t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    index = [list(map(int, input().split())) for _ in range(k)]
    cnt = 0
    arr = [[0] * m for _ in range(n)]
    q = []
    visited = [[0] * m for _ in range(n)]
    for j in range(k):
        arr[index[j][1]][index[j][0]] = 1
    for j in range(k):
        if arr[index[j][1]][index[j][0]] == 1:
            si = index[j][1]
            sj = index[j][0]
            cnt += 1
            visited[si][sj] = 1
            q.append((si, sj))
            worm()
    print(cnt)