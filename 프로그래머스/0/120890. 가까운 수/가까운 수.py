def solution(array, n):
    array.sort()
    new_array = list(map(lambda x : n - x, array))
    answer = [i if i >= 0 else -i for i in new_array ]
    return array[answer.index(min(answer))]