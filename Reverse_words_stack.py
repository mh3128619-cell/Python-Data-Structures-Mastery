from collections import deque

def reverse_words(sentence):
    stack = deque()
    result = []
    
    for i in range(len(sentence)):
        if sentence[i] != " ":
            stack.append(sentence[i])
        else:
            while stack:
                result.append(stack.pop())
            result.append(" ")
            
    while stack:
        result.append(stack.pop())
        
    return "".join(result)

input_sentence = "Hello World"
print(reverse_words(input_sentence))
