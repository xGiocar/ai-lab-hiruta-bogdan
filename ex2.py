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