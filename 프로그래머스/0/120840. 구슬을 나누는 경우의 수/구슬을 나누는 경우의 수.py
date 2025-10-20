def solution(balls, share):
    balls_c = 1
    balls_s = 1
    for i in range(share):
        balls_c *= (balls-i)
        balls_s *= (share-i)
    return balls_c/balls_s