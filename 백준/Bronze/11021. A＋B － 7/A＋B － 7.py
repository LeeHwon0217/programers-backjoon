T = int(input())
li = []

for i in range(T):
    a, b = map(int, input().split())
    li.extend([[a, b]])

# print(li)
# Case #1: 2

for n, j in enumerate(li):
    print(f'Case #{n+1}: {sum(j)}')