def remove_consecutive_duplicates(string):
    stack = []
    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)

print(remove_consecutive_duplicates("aabccba"))
print(remove_consecutive_duplicates("aaabccdddde"))
