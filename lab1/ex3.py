numbers = [3,5,7,1,2,8,5,3,8,3]
#numbers = [1,2,3,4,5]
sum = 0
n = len(numbers)

for i in range(n - 2):
    sum += numbers[i]

print(sum)