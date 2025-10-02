def solution(n):
    if n%2 == 0:
        return (2+n)/4*n
    else:
        return (1+n)/4*(n-1)