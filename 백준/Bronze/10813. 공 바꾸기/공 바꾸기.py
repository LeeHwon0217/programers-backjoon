n, m = map(int, input().split())
li =[]
answer = ''

for a in range(1, n+1):
    li.append(a)

for b in range(m):
    t = 0
    i, j = map(int, input().split())
    t = li[i-1]
    li[i-1] = li[j-1]
    li[j-1] = t

print(' '.join(map(str, li)))