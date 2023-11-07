
import numpy as np

DNA_samples = [' ACCATACCTTCGATTGTCGTGGCCACCCTCGGATTACACGGCAGAGGTGC ',
 ' GTTGTGTTCCGATAGGCCAGCATATTATCCTAAGGCGTTACCCCAATCGA ',
 ' TTTTCCGTCGGATTTGCTATAGCCCCTGAACGCTACATGCACGAAACCAC ',
 ' AGTTATGTATGCACGTCATCAATAGGACATAGCCTTGTAGTTAACAG ',
 ' TGTAGCCCGGCCGTACAGTAGAGCCTTCACCGGCATTCTGTTTG ',
 ' ATTAAGTTATTTCTATTACAGCAAAACGATCATATGCAGATCCGCAGTGCGCT ',
 ' GGTAGAGACACGTCCACCTAAAAAAGTGA ',
 ' ATGATTATCATGAGTGCCCGGCTGCTCTGTAATAGGGACCCGTTATGGTCGTGTTCGATCAGAGCGCTCTA ',
 ' TACGAGCAGTCGTATGCTTTCTCGAATTCCGTGCGGTTAAGCGTGACAGA ',
 ' TCCCAGTGCACAAAACGTGATGGCAGTCCATGCGATCATACGCAAT ',
 ' GGTCTCCAGACACCGGCGCACCAGTTTTCACGCCGAAAGCATC ',
 ' AGAAGGATAACGAGGAGCACAAATGAGAGTGTTTGAACTGGACCTGTAGTTTCTCTG ',
 ' ACGAAGAAACCCACCTTGAGCTGTTGCGTTGTTGCGCTGCCTAGATGCAGTGG ',
 ' TAACTGCGCCAAAACGTCTTCCAATCCCCTTATCCAATTTAACTCACCGC ',
 ' AATTCTTACAATTTAGACCCTAATATCACATCATTAGACACTAATTGCCT ',
 ' TCTGCCAAAATTCTGTCCACAAGCGTTTTAGTTCGCCCCAGTAAAGTTGT ',
 ' TCAATAACGACCACCAAATCCGCATGTTACGGGACTTCTTATTAATTCTA ',
 ' TTTTTCGTGGGGAGCAGCGGATCTTAATGGATGGCGCCAGGTGGTATGGA ']

"""
1) sigma the set of letter "alphabet"
2) Epsilon the empty word
3) An operation . concatanation

Words of length n, sigma^n
sigma^n = { a . w, a within sigma, w within sigma^n-1 }
sigma_0 = {epsilon}
sigma_1 = { a . epsilon, a within sigma }
sigma* = union sigma

4) abs(w) = n such that w within sigma^n 
'number of letter in the word'

Notation : 
if w within sigma*, and abs(w) = n
w = w1 * w2*...wn with wi within sigma
v = v1*...vn

Define Hamming:

For a given n, for each w,v within sigma^n
H(w,v) = "number of differences at each position in the words"
sigma^n (delta wi,vj)
delta(a,b) = 1 if a != b and = 0 if a = b

"""

#TASK 1
def hamming(w, v):
    distance = 0
    for i in range(len(w)):
        if w[i] != v[i]:
            distance +=1
    return distance

print(hamming(DNA_samples[0], DNA_samples[1]))

#TASK 2

def levenshtein(s1,s2):
    m, n = len(s1), len(s2)
    d = np.zeros((m + 1,n + 1))
    for i in range(1,m + 1):
        d[i, 0] = i
    for j in range(1,n + 1):
        d[0,j] = j
    print(d)
    for j in range(1, n+1):
        for i in range(1,m+1):
            insertCost = d[i - 1, j] + 1
            deleteCost = d[i, j - 1] + 1
            if s1[i-1] == s2[j-1]:
                subCost = d[i - 1, j - 1]

            else:
                subCost = d[i - 1, j - 1] + 1
            d[i,j] = min(insertCost, deleteCost, subCost)
    return d[m,n]

print(levenshtein("kryptonite", "python"))

n = len(DNA_samples)
M = np.zeros((n,n))
print(n, M)
for i in range(n):
    for j in range(n):
        M[i][j] = levenshtein(DNA_samples[i], DNA_samples[j])

print(M[0][:], M[:][0])