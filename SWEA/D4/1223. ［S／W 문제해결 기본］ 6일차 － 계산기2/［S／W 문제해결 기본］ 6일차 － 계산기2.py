T = 10

def prec(op):
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0

for tc in range(1, T + 1):
    l = int(input().strip())
    base = input().strip()

    out = []
    stack = []

    for ch in base:
        if ch.isdigit():
            out.append(ch)
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                out.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()
        else:
            while stack and stack[-1] != '(' and prec(stack[-1]) >= prec(ch):
                out.append(stack.pop())
            stack.append(ch)

    while stack:
        out.append(stack.pop())

    stack.clear()

    for ch in out:
        if ch.isdigit():
            stack.append(ch)
        else:
            if ch == "*":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b*a)
            elif ch == "+":
                a = int(stack.pop())
                b = int(stack.pop())
                stack.append(b + a)

    print(f"#{tc}",stack[0])