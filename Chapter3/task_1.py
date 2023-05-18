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
put_list()