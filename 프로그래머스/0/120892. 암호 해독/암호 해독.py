def solution(cipher, code):
    return ''.join(cipher[code*(i+1) - 1] for i in range(len(cipher)) if len(cipher) >= code*(i+1))