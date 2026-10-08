# ex 1 - array elements average

n = int(input())
sum = 0

if n == 0:
    print ("Can't handle empty list")
    exit()

for i in range (n):
    x = int(input())
    sum += x

mean = sum / n
print(mean)

# ex 2 - separate odd from even
nums = [1, 2, 3, 4, 5, 6, 7, 8]

odd = []
even = []

for x in nums:
    if x % 2 == 0:
        odd += [x]
    else:
        even += [x]

print(odd)
print(even)

# ex 3 - sum of n - 2 numbers
numbers = [3,5,7,1,2,8,5,3,8,3]
#numbers = [1,2,3,4,5]
sum = 0
n = len(numbers)

for i in range(n - 2):
    sum += numbers[i]

print(sum)

# ex 4 - filter even indexed elements from array
nums = [3,4,6,8,2,5,9]

n = len(nums)
result_list = []

for i in range(n):
    if i % 2 != 0:
        result_list += [nums[i]]

print(result_list)

# ex 5 - find minimum from array
nums = [3,5,6,2,7,1,-7,2,7,-5]
min = nums[0]
n = len(nums)

for i in range (1, n):
    if nums[i] < min:
        min = nums[i]

print(min)