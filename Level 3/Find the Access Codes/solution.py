def solution(l):
    tri = 0
    c= [0] * len(l)
    for i in range(0,len(l)):
        j=0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                tri += c[j]
    return tri