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