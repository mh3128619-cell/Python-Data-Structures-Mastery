def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token.isdigit():
            stack.append(int(token))
        else:
            val2 = stack.pop()
            val1 = stack.pop()
      
            if token == '+': stack.append(val1 + val2)
            elif token == '-': stack.append(val1 - val2)
            elif token == '*': stack.append(val1 * val2)
            elif token == '/': stack.append(val1 / val2)
            
    return stack[0]

print(evaluate_postfix("2 3 1 * + 9 -"))
