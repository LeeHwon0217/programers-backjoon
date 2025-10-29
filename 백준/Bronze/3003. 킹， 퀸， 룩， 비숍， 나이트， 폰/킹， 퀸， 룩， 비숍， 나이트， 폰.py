# 킹 퀸 룩 비숍 나이트 폰
# 1  1  2  2    2    8

li = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

# print(li)
# print(chess)

print(' '.join(map(str, list(map((lambda x, y: y-x), li, chess)))))