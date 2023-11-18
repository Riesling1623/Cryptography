# Chinese Remainder Theorem

# Using the existence construction
def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = egcd(b % a, a)
        return gcd, y - (b // a) * x, x

''' 
x ≡ 2 mod 5
x ≡ 3 mod 11
x ≡ 5 mod 17
'''

def crtheorem(a1, n1, a2, n2):
    bez = egcd(n1, n2) # find bezout coefficients
    m1 = bez[1]
    m2 = bez[2]

    # return n2 and a2 for the next step
    return (n1*n2), (a1*m2*n2 + a2*m1*n1 + n1*n2) % (n1*n2)

a = [2,3,5]
n = [5,11,17]

tmp = crtheorem(a[0], n[0], a[1], n[1])
n2 = tmp[0]
a2 = tmp[1]
res = crtheorem(a[2], n[2], a2, n2)
print(res[1])