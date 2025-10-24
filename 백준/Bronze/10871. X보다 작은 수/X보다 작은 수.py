n, x = map(int, input().split())
li = list(map(int, input().split()))

li = list(filter(lambda a: a < x, li))
print(' '.join(map(str, li)))