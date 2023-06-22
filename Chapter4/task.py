LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "勉強は好き？"],
    [3, 4, "運動は好き？"],
    [5, 6, "数学は好き？"],
    [None, None, "普通校の学校がおすすめ"],
    [None, None, "体育系の学校がおすすめ"],
    [None, None, "文系の学校がおすすめ"],
    [None, None, "理数系の学校がおすすめ"],
]

i = 0
while node[i][LEFT] and node[i][RIGHT]:
    s = input(f'{node[i][DATA]}(Y/n): ').lower()
    if s == 'y':
        i = node[i][RIGHT]
    elif s == 'n':
        i = node[i][LEFT]
print(f'診断結果: {node[i][DATA]}')