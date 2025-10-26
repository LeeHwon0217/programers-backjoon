S = input()
li = []

spell = sorted('abcdefghijklmnopqrstuvwxyz')

for i, v in enumerate(spell):
    if v in S:
        li.append(S.index(v))
    else:
        li.append(-1)

print(' '.join(map(str, li)))