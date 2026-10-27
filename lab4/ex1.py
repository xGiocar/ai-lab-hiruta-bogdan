lst = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41.0], ["Harsh", 39.0]]

lowest = 101
second_lowest = 101

lst.sort(key=lambda x: x[1])

students = []

for elem in lst:
    if lowest == 101:
        lowest = elem[1]
    if elem[1] > second_lowest:
        break
    if elem[1] > lowest:
        second_lowest = elem[1]
    
    if elem[1] == second_lowest:
        students.append(elem)
    

students.sort(key=lambda x: x[0])

print(students)
        
        