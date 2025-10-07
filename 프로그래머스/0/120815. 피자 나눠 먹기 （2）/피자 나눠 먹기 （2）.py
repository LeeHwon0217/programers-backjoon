def solution(n):
    div = max(i for i in [1, 2, 3, 6] if n%i == 0)
    return div*(n//div)*(6//div)//6