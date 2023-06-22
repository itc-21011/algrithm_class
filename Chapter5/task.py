data = ["あ","さ","た","か","な"]

print(data, "元のデータ")

for i in range(0, 4):
    m = i
    for j in range(i+1, 5):
        if data[j] < data[m]:
            m = j
    data[i], data[m] = data[m], data[i]

print(data, "ソート後のデータ")