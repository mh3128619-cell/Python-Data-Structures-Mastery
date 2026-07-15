def next_greater_element(nums):
    result = [-1] * len(nums)
    stack = []

    for i in range(len(nums)):
        while stack and nums[i] > nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        
        stack.append(i)

    return result

numbers = [4, 5, 2, 10]
print(f"Original list: {numbers}")
print(f"Next Greater Elements: {next_greater_element(numbers)}")
