nums = [10, 20, 30, 40, 50]
new_list = []

for i in range(len(nums) - 1, -1, -1):
    new_list.append(nums[i])

print(new_list)
