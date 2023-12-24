"""
    CryptoHack - Elliptic Curves
    Point Addition Solution
"""

from Crypto.Util.number import inverse

def addTwoPoints(X, Y, a, p):
    if (X[0] == 0) and (X[1] == 0):
        return Y
    elif (Y[0] == 0) and (Y[1] == 0):
        return X
    elif (X[0] == Y[0]) and (X[1] + Y[1] == p):
        return 0
    else:
        if (X[0] == Y[0]) and (X[1] == Y[1]):
            lb = (3*(X[0]**2)+a) * (inverse(2*X[1], p))
        else:
            lb = (Y[1]-X[1]) * (inverse(Y[0]-X[0], p))
        x3 = lb**2 - X[0] - Y[0]
        y3 = lb*(X[0]-x3) - X[1]
        return x3%p, y3%p

if __name__ == "__main__":
    P = (493, 5564)
    Q = (1539, 4742)
    R = (4403,5202)
    a = 497
    p = 9739
    PP = addTwoPoints(P, P, a, p) # P + P
    PPQ = addTwoPoints(PP, Q, a, p) # P + P + Q
    res = addTwoPoints(PPQ, R, a, p) # P + P + Q + R
    print(res)