nums = [3,4,6,8,2,5,9]

n = len(nums)
result_list = []

for i in range(n):
    if i % 2 != 0:
        result_list += [nums[i]]

print(result_list)