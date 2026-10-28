dic = dict()

with open("ex4.txt", 'r') as file:
    words = file.read().split()
    for word in words:
        if word not in dic:
            dic[word] = words.count(word)

print(dic)
