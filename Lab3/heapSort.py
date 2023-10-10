# Heap Sort

import random
import timeit

n = int(input("Enter the size of the array"))
arr = []

for i in range(n):
    num = random.randint(1, 30)
    arr.append(num)


def heapifyFunc(arr, n, i):
    maxIdx = i  #creating the maxIndex
    leftChild = 2*i+1
    rightChild = 2*i+2
    if(leftChild<n and arr[leftChild]>arr[maxIdx]):
        maxIdx = leftChild
    if(rightChild<n and arr[rightChild]>arr[maxIdx]):
        maxIdx = rightChild
    if(maxIdx!=i):
        # temp = arr[i]
        # arr[i] = arr[maxIdx]
        # arr[maxIdx] = temp
        (arr[i], arr[maxIdx]) = (arr[maxIdx], arr[i])
        heapifyFunc(arr, n, maxIdx)

def heapSort(arr, n):
    # for Building the maxHeap
    for i in range(n//2-1, -1, -1):
        heapifyFunc(arr, n, i)
    
    # for pushing the larget at the end
    for i in range(n-1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapifyFunc(arr, i, 0)

start = timeit.default_timer()
heapSort(arr, n)
for i in range(n):
    print(arr[i],end=" ")

end = timeit.default_timer()
print("\n")
print("Time taken by heap sort is :",(end-start)*1e3)

    
