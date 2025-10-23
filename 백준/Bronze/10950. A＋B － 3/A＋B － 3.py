t = int(input())
answer = []
for i in range(t):
    answer.append(list(map(int, input().split())))

for j in answer:
    print(sum(j))