MAX = 5
data = [None]*MAX
pointer = [None]*MAX
head = 0
strings = ['東京', '大阪', '福岡', '名古屋']

def add_list(d):
    n = -1
    for i in range(MAX):
        if data[i] == None:
            n = i
            break
    if n == -1:
        print("データ領域に空きがありません")
        return False
    for i in range(MAX):
        if data[i] != None and pointer[i]==None:
            pointer[i] = n
            break
    data[n] = d
    pointer[n] = None
    print("データ", d, "を追加しました")
    return True

def del_list(d):
    global head
    n = -1
    for i in range(MAX):
        if data[i] == d:
            n = i
            break
    if n == -1:
        print("そのデータは存在しません")
        return False
    if n != head:
        for i in range(MAX):
            if pointer[i] == n:
                pointer[i] = pointer[n]
    else:
        head = pointer[n]
        if head == None:
            head = 0
    data[n] = None
    pointer[n] = None
    print("データ", d, "削除しました")
    return True


def put_list():
    p = head
    while True:
        print(data[p], end="→")
        if pointer[p] == None:
            print("EOF")
            break
        p = pointer[p]

for string in strings:
    add_list(string)
del_list('大阪')
del_list('名古屋')
add_list('大阪')
add_list('名古屋')
put_list()