# ex 1

price = {"apples": 10, "milk": 12, "bread": 5}
mylist = [("apples", 2), ("milk", 2)]

shoping_list = [price[item] * quantity for item, quantity in mylist]

print(shoping_list)

# ex 2

friends = [("andrew", 10), ("george", 20), ("andrew", 5), ("ann", 10)]

friend_set = set()

for friend in friends:
    friend_set.add(friend[0])

print(friend_set)

# ex 3

x = int(input())
result = []

if x % 2 == 0:
    result = [y for y in range(x + 1)]
else:
    result = [y ** 2 for y in range(x + 1)]

print(result)

# ex 4

s_in = input()
num_in = int(input())
length = len(s_in)

dictionary = dict()

for i in range(num_in):
    dictionary[i] = s_in[i % length]

print(dictionary)
