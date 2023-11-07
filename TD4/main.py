import random
import numpy as np

def insertinSort(arr):
    i = 1
    while i <= len(arr) - 1:
        x = arr[i]
        j = i
        print(i, arr, j, arr[j - 1], x)
        while j > 0 and arr[j - 1] > x:
            arr[j] = arr[j - 1]
            j = j -1
            print(arr)
        arr[j] = x
        i = i + 1
    print(arr)
    return arr

def compare_price(correct, guess):
    if guess < correct:
        return -1
    elif guess > correct:
        return 1
    else:
        return 0
    
def thePriceIsRight():
    correct = random.randrange(0, 1000, 1)
    guess = int(input("Try a guess : "))
    tries = 1
    while guess != correct:
        if guess > correct: 
            guess = int(input("Too big, try again : "))
        if guess < correct: 
            guess = int(input("Too small, try again : "))
        tries+=1
    print(f"You guessed right in {tries} tries!")
    return tries


# Q3.
# How many times can i divide by two until there is 2 elements left ?
# We can consider an interval [0, n-1] with n = 2^k - 1
# we consider the middle of 0 and n - 1 : (n-1) / 2 = 2^(k-1) - 1,
#depending on the ordering relationship we will inspect the interval [0, 2^(k-1) - 1]
# or [2^(k-1) - 1, 2^k -1]
# We can prove that the number of guess G(n) = G(2^k -1) = H(k)
# G(n) = 1 + G(2^(k-1) -1) = 1 + G((n-1)/2)
# H(k) = 1 + H(k-1)
# => H is an arithmetic sequence H(k) = H(0) + k
# H(k) = O(k) = O(log(n))
# H(k) = 1 + k
# in our example we can prove that the number of steps is
# integer(log_2(1000) + 1) = 10
# 1024 = 2^10


# 2. HEAPSORT

def heapSort(arr):
    heap = [0] * len((arr))

    for j in range(len(arr) - 1):
        highest = 0

        for i in range(j, len(arr) - 1):
            if highest < arr[i]:
                highest = arr[i]

        if j == 0: # define the root, parent of all
            heap[j] = highest
        

    print(arr)

arr = [100, 19, 36, 17, 3, 25, 1, 2, 7]

def siftDown(arr, start, end):
    root = start
    while 2*root + 1 <= end:
        print(arr)
        child = 2*root + 1
        sw = root
        if arr[sw] < arr[child]:
            sw = child
        if child + 1 < end and arr[sw] < arr[child + 1]:
            sw = child + 1
        if sw == root:
            return arr
        else:
            arr[root], arr[sw] = arr[sw], arr[root]
            root = sw
    return arr

arr2 = [7,19,36,17,3,25,1,1]
siftDown(arr2, 0, len(arr2))

# SiftDown complexity is linked with the number of levels in the binary tree.
# for a heap, the leaves (the nodes without children) are at level h or h - 1
# Then 2^(h - 1) <= n <= 2^h - 1
# h = O(log_2(n)) = Complexity of Siftdown

def heapify(arr, end):
    start = (end - 1) / 2
    while start >= 0:
        print(len(arr) - 1)
        arr = siftDown(arr, start, len(arr) -1)
        start = start - 1
    return arr

arr3 = [42, 73, 12, 1, 10, 83]
heapify(arr3, len(arr3))


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
plssc("marseille","millenium")
def matrix_plssc(t,s):
    M = np.zeros(len(t), len(s))
    for row in M:
        for column in M[row]:
            M[row, column] = plssc(t[row:],s[column:])
    return M


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