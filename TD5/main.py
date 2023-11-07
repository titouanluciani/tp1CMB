import numpy as np

def merge(T1, T2):
    n1 = len(T1)
    n2 = len(T2)
    if n1 == 0:
        return T1
    if n2 == 0:
        return T2
    
    if T1[0] < T2[0]:
        return [T1[0], merge(T1[2:n1], T2)]
    return merge(T2, T1) # equivalent with [T2[1], merge(T1, T2[2:n2])]

def plssc(t,s):
    if len(min(t, s)) == 0:
        return ''
    if t[0] == s[0]:
        return t[0] + plssc(t[1:], s[1:])
    else:
        return max(plssc(t[1:], s), plssc(t, s[1:]))
    
print(plssc("marseille","millenium"))

def matrix_plssc(t,s):
    M = np.full((len(t) + 1, len(s) + 1), "")
    print(M)
    for row in range(len(t) - 1, 0, -1):
        for column in range(len(s) - 1, 0, -1):
            if t[row] == s[column]:
                M[row, column] = t[row] + M[row + 1, column + 1]
            else:
                M[row, column] = max(M[row + 1, column], M[row, column + 1])
            
    return M

print(matrix_plssc("marseille","millenium"))

"""
empire, mere : 
mpire, ere
pire, re
ire, e

marseille, paris
arseille, aris
rseille, ris
seille, is
eille, s

marseille, millenium
arseille, illenium
rseille, llenium
seille, lenium
eille, enium




"""