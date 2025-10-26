T = int(input())
li = []

for a in range(T):
    R, S = input().split()
    answer=''
    for i in range(len(S)):
        answer += S[i]*int(R)
    li.append(answer)

    # print(answer)
print('\n'.join(li))
