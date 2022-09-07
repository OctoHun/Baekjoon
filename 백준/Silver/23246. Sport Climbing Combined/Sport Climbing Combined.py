n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
a = [0] * n
b = [0] * n
for i in range(n):
    a[i] = arr[i][1] * arr[i][2] * arr[i][3]
    b[i] = arr[i][1] + arr[i][2] + arr[i][3]
for i in range(n):
    for j in range(i+1, n):
        if a[i]>a[j]:
            a[i], a[j] = a[j], a[i]
            arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
            b[i], b[j] = b[j], b[i]
        elif a[i]==a[j]:
            if b[i]>b[j]:
                a[i], a[j] = a[j], a[i]
                arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
                b[i], b[j] = b[j], b[i]
            elif b[i]==b[j]:
                if arr[i][0]>arr[j][0]:
                    a[i], a[j] = a[j], a[i]
                    arr[i][0], arr[j][0] = arr[j][0], arr[i][0]
                    b[i], b[j] = b[j], b[i]
for i in range(3):
    print(arr[i][0], end = ' ')