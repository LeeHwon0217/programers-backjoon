recipt = int(input())
n = int(input())
li = []
total = 0

for i in range(n):
    li.append(list(map(int, input().split())))

for j in li:
    total += j[0] * j[1]

print('Yes' if recipt == total else 'No')