def binary(s):
    if s == "1":
        return
    count = 0
    for j in s:
        if j == "1":
            count += 1
        else:
            answer[1] += 1
    answer[0] += 1
    binary(bin(count).replace("0b", ""))
    
    

def solution(s):
    global answer
    answer = [0, 0]
    binary(s)
    return answer