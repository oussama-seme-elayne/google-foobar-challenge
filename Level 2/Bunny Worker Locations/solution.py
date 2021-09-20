def solution(x, y):
    a = y-1
    b = x+a
    id = b*(b+1)//2
    id -= a
    return str(id)