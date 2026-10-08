# ex 1

price = {"apples": 10, "milk": 12, "bread": 5}
mylist = [("apples", 2), ("milk", 2)]

shoping_list = [price[item] * quantity for  item, quantity in mylist]

print(shoping_list)

# ex 2

friends = [("andrew", 10), ("george", 20), ("andrew", 5), ("ann", 10)]

friend_set = set()

for friend in friends:
    friend_set.add(friend[0])

print(friend_set)