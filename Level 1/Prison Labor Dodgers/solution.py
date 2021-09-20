def solution(x, y):
    if(len(x)>len(y)):
        for i in x:
            if i in y:
                continue
            else:
                break
    else:
        for i in y:
            if i in x:
                continue
            else:
                break
    return i