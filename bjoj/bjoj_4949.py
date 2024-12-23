# 문자열 입력 받기(.나올때 까지)
# 각 줄 검사
# list에 넣고 빼기

while(True):
    str = input()
    if str == '.':
        break
    stack = []
    balanced = True

    for char in str:
        if char in "([":
            stack.append(char)
        elif char == ")":
            if not stack or stack[-1] != "(":
                balanced = False
                break
            stack.pop()
        elif char == ']':
            if not stack or stack[-1] != "[":
                balanced = False
                break
            stack.pop()

    if stack:
        balanced = False
    if balanced:
        print("yes")
    else:
        print("no")