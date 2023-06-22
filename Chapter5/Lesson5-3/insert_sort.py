data = [9, 4, 7, 2, 3, 8, 6, 1, 5, 0]
n = len(data)
print(data, "元のデータ")

for i in range(1, n):
    tmp = data[i]
    j = i
    while j>0 and data[j-1]>tmp:
        data[j] = data[j-1]
        j = j - 1
    data[j] = tmp

print(data, "ソート後のデータ")