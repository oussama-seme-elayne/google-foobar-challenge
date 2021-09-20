from itertools import combinations
def solution(num_buns, num_required):
    bunny = [[] for i in range(num_buns)]
    if num_required == 0:
        return bunny
    start = 0
    for c in combinations(bunny, num_buns - num_required + 1):
        for item in c:
            item.append(start)
        start += 1
    return bunny
    [[0], [1], [2], [3]]