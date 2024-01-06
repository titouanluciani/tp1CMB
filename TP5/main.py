
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

distance = hamming(DNA_samples[0], DNA_samples[1])
print(distance)

#TASK 2

def levenshtein(seq1,seq2):
    m, n = len(seq1), len(seq2)
    d = np.zeros((m + 1,n + 1))
    for i in range(1,m + 1):
        d[i, 0] = i
    for j in range(1,n + 1):
        d[0,j] = j
    for j in range(1, n+1):
        for i in range(1,m+1):
            insertCost = d[i - 1, j] + 1
            deleteCost = d[i, j - 1] + 1
            if seq1[i-1] == seq2[j-1]:
                subCost = d[i - 1, j - 1]

            else:
                subCost = d[i - 1, j - 1] + 1
            d[i,j] = min(insertCost, deleteCost, subCost)
    return d[m,n]

print(levenshtein("kryptonite", "python"))

n = len(DNA_samples)
M = np.zeros((n,n))
for i in range(n):
    for j in range(n):
        M[i][j] = levenshtein(DNA_samples[i], DNA_samples[j])

print(M)
np.savetxt("levenshtein_matrix.txt", M, fmt='%d')


def smith_waterman(seq1, seq2, match_score=3, gap_cost=2):
    m, n = len(seq1), len(seq2)
    H = np.zeros((m+1, n+1))

    max_score = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            match = H[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else - match_score)
            delete = H[i-1][j] - gap_cost
            insert = H[i][j-1] - gap_cost
            H[i][j] = max(0, match, delete, insert)
            if H[i][j] > max_score:
                max_score = H[i][j]

    return H, max_score

# Task 4: Test Smith-Waterman Algorithm

H, max_score = smith_waterman(DNA_samples[0], DNA_samples[1])
print(H, max_score)

# Task 5: Modify Output of Smith-Waterman Algorithm

def smith_waterman_modified(H, seq1, seq2, match_score=3):
    alignment1, alignment2 = '', ''
    i, j = np.unravel_index(np.argmax(H), H.shape)
    while H[i][j] > 0:
        current_score = H[i][j]
        if i > 0 and j > 0 and H[i][j] == H[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else - match_score):
            alignment1 = seq1[i-1] + alignment1
            alignment2 = seq2[j-1] + alignment2
            i -= 1
            j -= 1
        elif i > 0 and H[i][j] == H[i-1][j] - match_score:
            alignment1 = seq1[i-1] + alignment1
            alignment2 = '-' + alignment2
            i -= 1
        else:
            alignment1 = '-' + alignment1
            alignment2 = seq2[j-1] + alignment2
            j -= 1

    return alignment1, alignment2

alignment1, alignment2 = smith_waterman_modified(H, DNA_samples[0], DNA_samples[1])
print(alignment1, alignment2)

# Task 6: Needleman-Wunsch Algorithm

def needleman_wunsch(seq1, seq2, match_score=3, gap=2):
    m, n = len(seq1), len(seq2)
    H = np.zeros((m+1, n+1))

    for i in range(m+1):
        H[i][0] = -i * gap
    for j in range(n+1):
        H[0][j] = -j * gap

    for i in range(1, m+1):
        for j in range(1, n+1):
            match = H[i-1][j-1] + (match_score if seq1[i-1] == seq2[j-1] else - match_score)
            delete = H[i-1][j] - gap
            insert = H[i][j-1] - gap
            H[i][j] = max(match, delete, insert)

    return H, H[m][n]

H_global, max_score_global = needleman_wunsch(DNA_samples[0], DNA_samples[1])
print(H_global, max_score_global)