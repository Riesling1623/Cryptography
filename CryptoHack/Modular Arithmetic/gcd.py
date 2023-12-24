def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

if __name__ == "__main__":
    a = 17
    b = 1515
    print(gcd(a,b))