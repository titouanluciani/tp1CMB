# QUESTION 5
# A : m,n  B : n,p  C : p, r
# Matrice mxn dot nxp : ((m * n) * p) * m : AB : m,p
# (AB)C : mnp + mpr : m,r
# A(BC) : mxn * (nxp * pxr) = mxn * (npr) = mxn * nxr + npr = mnr + npr
# (A1*A2*..*Ak)(Ak+1*An)
# A1*(A2*...*An)
# (A1*A2)(A3*...*An)
# => recursive formula

# Compute dimension's formula
# l1*c1*
# C(n) = sum( C(k) * C(n-k)) => exponential complexity
# Proof : 1) C(n) Catalan numbers : 
# 2) Prove that C(n) > 2^n, C(1) = 2

# sequence d0, d1...dn of A0,A1...An : Ai has dimension di-1xdi
# M[i,j] number of multiplication (Ai...Aj)

# (Ai...Ak)(Ak+1...Aj)
#   M[i,k] + M[Ak+1, Aj]
#        + di*dk*dj #(multiplication of the two blocks)
# M[0,0] = 0 ; M[n,n] = 0

# QUESTION 9
# 1 :  Idea : do it diagonal by diagonal
# 2 : For M[i,j], apply  the update rule.

import numpy as np

def optimal_multiplication(dimensions):
    n = len(dimensions)
    M = np.zeros((n,n))

    for diag in range(2,n): #diagonal of the matrix
        for d in range(n - diag+1):
            i = d
            j = diag + d
            sp_multiplications = []
            for k in range(i,j):
                value = M[i,k] + M[k+1,j] + dimensions[i-1]*dimensions[k]*dimensions[i]
                sp_multiplications.append(value)
            M[i,j] = np.min(sp_multiplications)
    return M[0,n-1]