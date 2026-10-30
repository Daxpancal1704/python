def check(text):
    stack = []
    depth = 0
    max_depth = 0

    pairs = {')': '(', ']': '[', '}': '{'}

    for i, ch in enumerate(text):
        if ch in "([{":
            stack.append((ch, i + 1))
            depth += 1
            max_depth = max(max_depth, depth)

        elif ch in ")]}":
            if not stack or stack[-1][0] != pairs[ch]:
                print("Invalid at position", i + 1)
                return

            stack.pop()
            depth -= 1

    if stack:
        print("Invalid at position", stack[0][1])
    else:
        print("Valid, max depth", max_depth)


text = input()
check(text)