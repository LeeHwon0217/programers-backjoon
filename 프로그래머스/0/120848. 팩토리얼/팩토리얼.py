def solution(n):
    mul = 1
    i = 1
    while(mul <= n):
        i += 1
        mul *= i
    return i-1