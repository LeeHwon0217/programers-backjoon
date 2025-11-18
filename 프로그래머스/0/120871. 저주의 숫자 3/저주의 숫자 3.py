def solution(n):
    count = 0
    for i in range(1, n+1):
        count += 1
        while count%3 == 0 or '3' in str(count):
            if count % 3 == 0:
                count += 1
            elif '3' in str(count):
                count += 1
    return count