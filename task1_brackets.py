s = input()

open_brack = "([{"
matching_open = {")": "(", "]": "[", "}": "{"}
stack = []
problem = None

for i, brack in enumerate(s):
    if brack in open_brack:
        stack.append((brack, i))
    elif brack in matching_open:
        if not stack or stack[-1][0] != matching_open[brack]:
            problem = (brack, i)
            break
        stack.pop()

if problem is None and stack:
    problem = stack[-1]

if problem is None:
    print("Balanced")
else:
    bracket, position = problem
    print(f"Problem at position {position}: {bracket}")
    print(s)
    print(" " * position + "^")