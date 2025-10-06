def solution(my_string):
    return sum(map(int, filter(str.isdigit, my_string)))