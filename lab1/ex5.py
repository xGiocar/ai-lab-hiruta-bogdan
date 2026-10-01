nums = [3,5,6,2,7,1,-7,2,7,-5]
min = nums[0]
n = len(nums)

for i in range (1, n):
    if nums[i] < min:
        min = nums[i]

print(min)