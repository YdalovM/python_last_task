a = [1, 2, 3, 12, 10, 4, 45, 34]

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] > a[j]:
           a[i], a[j] = a[j], a[i]
print(a)