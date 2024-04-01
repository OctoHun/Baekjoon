from collections import deque

def isbroken(string):
    for i in string:
        if int(i) in broken:
            return True
    return False


n = int(input())
m = int(input())
broken = 0
if m != 0:
    broken = list(map(int, input().split()))
else:
    broken = []
broken.sort()

# 첫 번째 방법: +, - 버튼으로만 채널 바꾸기
first = abs(n-100)

# 다 고장났으면 첫 번째 방법이 정답
if m == 10:
    print(first)
else:

    # 두 번째 방법: n보다 작은 수에서 +버튼으로 채널 바꾸기
    second = 999999999
    for i in range(n, -1, -1):
        if not isbroken(str(i)):
            second = len(str(i)) + n - i
            break

    # 세 번째 방법: n보다 큰 수에서 -버튼으로 채널 바꾸기
    third = 999999999
    maximum = min(first, second) + 1 + n
    for i in range(n, maximum):
        if not isbroken(str(i)):
            third = len(str(i)) + i - n
            break
    
    print(min(first, second, third))