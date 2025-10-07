def solution(numbers, direction):
    numbers = list(map(str, numbers))
    if direction == 'right':
        numbers.insert(0, str(numbers[-1]))
        del numbers[-1]
    else:
        a = str(numbers.pop(0))
        numbers.insert(len(numbers), a)
    return list(map(int, numbers))