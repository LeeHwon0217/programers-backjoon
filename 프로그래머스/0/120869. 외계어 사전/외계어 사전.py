def solution(spell, dic):
    for i in dic:
        count = 0
        if len(spell) == len(i):
            for j in spell:
                if j in i:
                    count += 1
            if count == len(spell):
                return 1
    return 2