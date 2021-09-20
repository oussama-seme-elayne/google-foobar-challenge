import math

def soln(num):
    if (num == 0):
      return 0
    sqrt = "414213562373095048801688724209698078569671875376948073176679737990732478462107038850387534327641572735013846230912297024924836055850737212644121497099935831"
    n = num
    note_prime = str(int(sqrt) * n)[:-156]
    if len(note_prime) == 0:
      note_prime = 0
    else:
      note_prime = int(note_prime)
    return (note_prime + n) * (note_prime + n + 1) / 2 - note_prime * (note_prime + 1) - soln(note_prime)

def solution(s):
    return str(int(soln(int(s))))