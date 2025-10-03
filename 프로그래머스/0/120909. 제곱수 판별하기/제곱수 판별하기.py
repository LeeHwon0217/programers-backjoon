import math

def solution(n):
    if math.ceil(math.sqrt(n)) == math.sqrt(n):
        return 1
    else:
        return 2