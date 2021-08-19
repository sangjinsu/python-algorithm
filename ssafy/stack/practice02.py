s1 = '()()((())))'

stack = []
result = 'OK'
for c in s1:
    if c == '(':
        stack.append('(')
    else:
        if stack:
            stack.pop()
        else:
            result = 'Error'

if stack:
    result = 'Error'

print(result)
