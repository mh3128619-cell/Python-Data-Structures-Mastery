from collections import deque

def is_balanced(expression):
    stack = deque()
    mapping = {")": "(", "}": "{", "]": "["}
    
    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return len(stack) == 0

print(f"'([])' is balanced: {is_balanced('([])')}")
print(f"'((])' is balanced: {is_balanced('((])')}")
print(f"'((()))' is balanced: {is_balanced('((()))')}")
