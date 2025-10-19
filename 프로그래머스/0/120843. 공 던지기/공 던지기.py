def solution(numbers, k):
    numbers = 2*numbers
    return numbers[2*(k-1)] if len(numbers) > 2*(k-1) else numbers[2*(k-1) % len(numbers)]