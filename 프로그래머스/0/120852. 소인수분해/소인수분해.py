def solution(n):
    answer = []
    temp = n
    while temp > 1:
        for i in range(2, temp+1):
            if temp % i == 0:
                answer.append(i)
                temp = temp//i
                break
    answer = set(answer)
    answer = list(answer)
    return sorted(answer)