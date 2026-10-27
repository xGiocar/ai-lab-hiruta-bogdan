ar1 = [1,10,9,10,8]
ar2 = [8,10,9,7,6]
ar3 = [10,9,10,7,6]

def has_seq(arr1, arr2):
    for i in range(len(arr1) - 2):
        for j in range(len(arr2) - 2):
            if arr1[i:(i+3)] == arr2[j:(j+3)]:
                return True
    return False

print(has_seq(ar1, ar2))
print(has_seq(ar1, ar3))
