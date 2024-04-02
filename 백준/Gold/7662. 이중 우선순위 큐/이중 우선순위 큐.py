import sys
import heapq

T = int(sys.stdin.readline())
answer = ""
for t in range(T):
    K = int(sys.stdin.readline())
    minheap = []
    maxheap = []
    all = {}
    flag = 0
    for k in range(K):
        line = list(sys.stdin.readline().split())
        if line[0] == "I":
            heapq.heappush(minheap, [int(line[1]), str(flag)])
            heapq.heappush(maxheap, [-int(line[1]), str(flag)])
            all[str(flag)] = True
            flag += 1
        elif line[1] == "1":
            while len(all) != 0:
                temp = heapq.heappop(maxheap)
                if str(temp[1]) in all:
                    del all[str(temp[1])]
                    break
        elif line[1] == "-1":
            while len(all) != 0:
                temp = heapq.heappop(minheap)
                if str(temp[1]) in all:
                    del all[str(temp[1])]
                    break
    if len(all) == 0:
        answer += "EMPTY\n"
    else:
        while True:
            temp = heapq.heappop(maxheap)
            if str(temp[1]) in all:
                answer += str(-temp[0])
                break
        answer += " "
        while True:
            temp = heapq.heappop(minheap)
            if str(temp[1]) in all:
                answer += str(temp[0])
                break
        answer += "\n"
print(answer)
    