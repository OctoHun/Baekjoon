n = int(input())
switch = list(map(bool, map(int, input().split())))
student = int(input())
st = [list(map(int, input().split())) for _ in range(student)]
for i in range(student):
    if st[i][0] == 1:
        for j in range(st[i][1]-1, n, st[i][1]):
            switch[j] = not switch[j]
    else:
        switch[st[i][1]-1] = not switch[st[i][1]-1]
        for j in range(1, (n+1)//2):
            if 0 <= st[i][1]-1-j < n and 0 <= st[i][1]-1+j < n and switch[st[i][1]-1-j] == switch[st[i][1]-1+j]:
                switch[st[i][1]-1 - j] = not switch[st[i][1]-1-j]
                switch[st[i][1]-1 + j] = not switch[st[i][1]-1+j]
            else:
                break
for i in range(n):
    if i != 0 and i % 20 == 0:
        print()
    print(int(switch[i]), end = ' ')