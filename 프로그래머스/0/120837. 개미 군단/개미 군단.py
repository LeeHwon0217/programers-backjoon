def solution(hp):
    d = 0
    b = 0
    i = 0
    d = hp//5
    b = (hp%5) // 3
    i = (hp%5) % 3
    return d + b + i