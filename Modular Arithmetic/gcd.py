def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    a = 26513
    b = 32321
    print(gcd(a,b))