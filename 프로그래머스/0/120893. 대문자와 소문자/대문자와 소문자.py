def solution(my_string):
    return ''.join(i.upper() if i != i.upper() else i.lower() for i in my_string )