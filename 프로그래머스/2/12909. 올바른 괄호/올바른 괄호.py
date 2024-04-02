from collections import deque

def solution(s):
    answer = True
    stack = deque()
    
    for i in s:
        if i == "(":
            stack.append(i)
        elif len(stack) == 0:
            return False
        else:
            stack.pop()
    
    if len(stack) == 0:
        return True
    return False