op = {
    '(': 0,
    '-': 1,
    '+': 1,
    '/': 2,
    '*': 2
}

m = '2+3*4/5'
stack = []
postfix = ''
for s in m:
    if '0' <= s <= '9':
        postfix += s
    else:
        if s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()
        else:
            while stack and op[s] <= op[stack[-1]]:
                postfix += stack.pop()
            stack.append(s)

while stack:
    postfix += stack.pop()

print(postfix)
