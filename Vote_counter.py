votes=["Ahmed","Sara","Ahmed","Mohamed","Sara","Ahmed"]
keys=3,2,1

count={}
for i in votes:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
