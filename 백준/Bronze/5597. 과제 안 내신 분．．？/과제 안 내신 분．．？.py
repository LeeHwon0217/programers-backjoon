li = []
first = 0

for i in range(28):
    li.append(int(input()))

li.sort()

for a, b in enumerate(li, 1):
    if a != b:
        first = b-1
        break

print(f'{first}\n{465 - sum(li) - first}')