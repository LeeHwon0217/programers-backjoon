import sys
input = sys.stdin.readline

T = int(input())
li = []

for i in range(T):
    a, b = map(int, input().split())
    li.extend([[a, b]])

# print(li)

for j in li:
    print(sum(j))