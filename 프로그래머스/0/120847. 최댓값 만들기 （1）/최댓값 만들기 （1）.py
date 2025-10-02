def solution(numbers):
    top = max(numbers)
    numbers.remove(top)
    second = max(numbers)
    return top*second