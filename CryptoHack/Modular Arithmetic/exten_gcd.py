# Find the inverse of 26513 (b) mod 32321 (a)

def inverse_mod(t, b, step):
    q.append(t//b)
    r = t % b
    
    # initialize p0 = 0 (p1 = 1)
    if (step == 0 or step == 1):
        p.append(step)
        step += 1
    else:
        p.append((p[step-2] - p[step-1] * q[step-2]) % a)
        step += 1
    
    if (r == 0):
        p.append((p[step-2] - p[step-1]*q[step-2]) % a)
    else:
        inverse_mod(b, r, step)

if __name__ == "__main__":
    a = 32321
    b = 26513
    # Since gcd(a,b) = 1, then the inverse of b exists. So p[-1] is the inverse of b mod a
    q = [] # quotient
    p = [] # inverse
    step = 0
    inverse_mod(a,b,step)
    print(p[-1])
    print("flag =",(1 - p[-1]*b)/a)