def solution(price):
    return int(0.8*price if price>=500000 else 0.9*price if price>=300000 else 0.95*price if price>=100000 else price)