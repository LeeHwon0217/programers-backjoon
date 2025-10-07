def solution(order):
    d = ['3', '6', '9']
    answer = 0
    for i in d:
        answer += str(order).count(i)
    return answer