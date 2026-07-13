text = "hello world"
count = {}

for i in text:
    if i != " ":
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

print(count)
