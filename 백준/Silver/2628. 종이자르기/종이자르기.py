x, y = map(int, input().split())
n = int(input())
col = [0] * 100
row = [0] * 100
row_cnt = 0
col_cnt = 0
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        row[row_cnt] = b
        row_cnt += 1
    else:
        col[col_cnt] = b
        col_cnt += 1
row[row_cnt] = y
col[col_cnt] = x
row_cnt += 1
col_cnt += 1
for i in range(row_cnt):
    for j in range(i+1, row_cnt):
        if row[i] > row[j]:
            row[i], row[j] = row[j], row[i]
for i in range(col_cnt):
    for j in range(i+1, col_cnt):
        if col[i] > col[j]:
            col[i], col[j] = col[j], col[i]
max_col = row[0]
max_row = col[0]
for i in range(1, row_cnt):
    if row[i] - row[i-1] > max_col:
        max_col = row[i] - row[i-1]
for i in range(1, col_cnt):
    if col[i] - col[i-1] > max_row:
        max_row = col[i] - col[i-1]
print(max_col * max_row)