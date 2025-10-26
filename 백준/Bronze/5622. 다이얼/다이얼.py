call = 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ'
S = input()
answer = 0
for i, v in enumerate(call, 3):
    for j in S:
        if j in v:
            answer += i

print(answer)