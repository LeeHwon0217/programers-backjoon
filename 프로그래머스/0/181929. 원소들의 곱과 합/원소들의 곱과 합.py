import math

def solution(num_list):
    mul = math.prod(num_list)
    # sum(iterable, start_value)
    pldoub = sum(num_list)**2
    return 1 if mul < pldoub else 0