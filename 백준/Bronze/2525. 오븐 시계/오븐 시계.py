a, b = map(int, input().split())
time = int(input())

total = 60*a + b + time
h = total//60
m = total%60

if h >= 24:
    h -= 24

print(h, m)