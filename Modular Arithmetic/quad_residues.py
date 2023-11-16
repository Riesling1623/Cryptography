p = 29
ints = [14 ,6, 11]

for a in range (1, p):
    a_square = a**2 % p
    if a_square in ints:
        print(a, a_square)
        break