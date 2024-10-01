import sys

def check_balanced(s):
    stack = []
    
    for char in s:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return "no"
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                return "no"
    
    # 스택이 비어 있어야 모든 괄호가 짝이 맞음
    if not stack:
        return "yes"
    else:
        return "no"

def getAnswer():
    input = sys.stdin.read
    data = input().splitlines()
    
    for line in data:
        if line == ".":
            break
        print(check_balanced(line))

getAnswer()