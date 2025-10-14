def solution(my_str, n):
    return [my_str[i*n:n*(i+1)] for i in range((len(my_str)-1)//n+1)]