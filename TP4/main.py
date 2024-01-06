import random
import time
import numpy as np
import matplotlib.pyplot as plt

def insertion_sort(arr):
    i = 1
    n = len(arr)
    while i < n:
        x = arr[i]
        j = i
        while j > 0 and arr[j- 1] > x:
            arr[j] = arr[j - 1]
            j = j - 1
        arr[j] = x
        i = i +1
    
    return arr

def bubble_sort(arr):
    t1 = time.time()
    i = 1
    n = len(arr)
    while i <= n - 1:
        j = i
        while j >= 0 and arr[j-1] > arr[j]:
            arr[j], arr[j - 1] = arr[j-1], arr[j]
            j = j - 1
        i+=1
    t2 = time.time()
    return arr, t2 - t1

def siftDown(arr, start, end):
    root = start
    while 2*root + 1 <= end:
        child = 2*root + 1
        sw = root
        if arr[sw] < arr[child]:
            sw = child
        if child + 1 <= end and arr[sw] < arr[child + 1]:
            sw = child + 1
        if sw == root:
            return arr
        else:
            arr[root], arr[sw] = arr[sw], arr[root]
            root = sw
    return arr


# SiftDown complexity is linked with the number of levels in the binary tree.
# for a heap, the leaves (the nodes without children) are at level h or h - 1
# Then 2^(h - 1) <= n <= 2^h - 1
# h = O(log_2(n)) = Complexity of Siftdown

def heapify(arr, end):
    start = (end - 1) // 2
    while start >= 0:
        arr = siftDown(arr, start, len(arr) - 1)
        start = start - 1
    return arr


def heapSort(arr):
    t1 = time.time()
    arr = heapify(arr, len(arr) - 1)
    end = len(arr) -1
    while end > 0:
        arr[end], arr[0] = arr[0], arr[end]
        end -= 1
        arr = siftDown(arr, 0, end)
    t2 = time.time()
    delta_t = t2 - t1
    return arr, delta_t


arr2 = [7,19,36,17,3,25,1,1]
arr3 = [42, 73, 12, 1, 10, 83]
arr = [100, 19, 36, 17, 3, 25, 1, 2, 7]

arr2 = siftDown(arr2, 0, len(arr2))
arr3 = heapify(arr3, len(arr3))

t1 = time.time()
arr, delta_t = heapSort(arr)
t2 = time.time()
#print(arr, delta_t, t2 - t1)

arr = insertion_sort(arr)
#print(arr)

arr, t_bubble = bubble_sort(arr)
#print(arr, t_bubble)

# 2. Complexxity in practice
# Q1. insertion_sort and bubble sort have a time complexity of n²
# Heapsort have a time complexity of nlog(n) : log(n) from siftsort and n from heapify
# Thus, heapsort is quicker.

# TASK 4 

N = []
insert = []
bubble = []
heapsort = []


for l in range(3, 13):
    n = 2**l
    N.append(l)

    arr = np.random.randint(400, size = n)

    t1 = time.time()
    arr_inser = insertion_sort(arr)
    arr = np.random.randint(400, size = n)

    t_inser = time.time()
    arr = np.random.randint(400, size = n)

    arr_bubble = bubble_sort(arr)
    t_bubble = time.time()

    arr_heapsort = heapSort(arr)
    t_heapsort = time.time()

    insert.append(t_inser - t1)
    bubble.append(t_bubble - t_inser)
    heapsort.append(t_heapsort - t_bubble)

plt.plot(N, insert, "blue", label="insert")
plt.plot(N, bubble, "red", label="bubble")
plt.plot(N, heapsort, "green", label="heapsort")
plt.legend()
plt.show()




# 3 SEARCH IN SORTED ARRAY

# TASK 6

def search(arr, e):
    i = 0
    while arr[i] != e and i < len(arr) - 1:
        i+=1
        if(arr[i] == e):
            return True
    
    return False


def dicho_search(arr, e, start, end):
    n = (end - start) // 2
    if arr[n] > e:
        dicho_search(arr, e, start, n - 1)
    if arr[n] < e:
        dicho_search(arr, e, n - 1, end)
    if arr[n] == e:
        return True

print(arr)
bool = dicho_search(arr, 2, 0, len(arr))
print(bool)