n, m = map(int, input().split())

li = list(i + 1 for i in range(n))

for a in range(m):
    i, j = map(int, input().split())
    li[i-1:j] = reversed(li[i-1:j])

print(' '.join(map(str, li)))