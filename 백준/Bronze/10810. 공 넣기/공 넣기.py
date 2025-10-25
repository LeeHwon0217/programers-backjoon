n, m = map(int, input().split())
li = [0] * n

for s in range(m):
    i, j, k = map(int, input().split())
    for b in range(i, j+1):
        li[b-1] = k

print(' '.join(map(str, li)))