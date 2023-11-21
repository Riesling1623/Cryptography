# Round Keys

from pwn import xor

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

def matrixflatten(matrix):
    """ Flatten the matrix """
    arr = []
    for i in range(len(matrix)):
        for ele in matrix[i]:
            arr.append(ele)
    
    return arr

def add_round_key(s, k):
    s = matrixflatten(s)
    k = matrixflatten(k)
    res = "".join([ xor(s[i], k[i]).decode() for i in range(len(s)) ])
    return res



print(add_round_key(state, round_key))

