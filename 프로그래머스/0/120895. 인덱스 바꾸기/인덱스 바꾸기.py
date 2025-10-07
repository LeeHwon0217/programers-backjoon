def solution(my_string, num1, num2):
    a = my_string[num1]
    b = my_string[num2]
    answer = ''.join(my_string[i] if i != num2 else a for i in range(len(my_string)))
    answer1 = ''.join(answer[i] if i != num1 else b for i in range(len(answer)))
    return answer1