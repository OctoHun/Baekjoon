bingo = [list(map(int, input().split())) for _ in range(5)]
arr = [list(map(int, input().split())) for _ in range(5)]
bingo_cnt = 0
cnt = 0
flag = 0
for i in range(5):
    for j in range(5):
        cnt += 1
        flag1 = 0
        for a in range(5):
            for b in range(5):
                if bingo[a][b] == arr[i][j]:
                    bingo[a][b] = 0
                    flag1 = 1
                    break
            if flag1 == 1:
                break
        if a == b:
            cnt0 = 0
            for x in range(5):
                if bingo[x][x] == 0:
                    cnt0 += 1
            if cnt0 == 5:
                bingo_cnt += 1
        if a + b == 4:
            cnt0 = 0
            for x in range(5):
                if bingo[x][4-x] == 0:
                    cnt0 += 1
            if cnt0 == 5:
                bingo_cnt += 1
        row_cnt0 = 0
        col_cnt0 = 0
        for x in range(5):
            if bingo[x][b] == 0:
                col_cnt0 += 1
            if bingo[a][x] == 0:
                row_cnt0 += 1
        if col_cnt0 == 5:
            bingo_cnt += 1
        if row_cnt0 == 5:
            bingo_cnt += 1
        if bingo_cnt > 2:
            flag = 1
        if flag == 1:
            break
    if flag == 1:
        break
print(cnt)