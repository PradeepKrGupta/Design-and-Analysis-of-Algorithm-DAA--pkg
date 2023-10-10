# Different sorting Algorithm functions
import random
import timeit

# first taking array and random elements
n = int(input("Enter the size of the array"))
arr = []

for i in range(n):
    num = random.randint(1,50)
    arr.append(num)


# Bubble sort
def bubbleSort(arr, n):
    for i in range(0, n):
        for j in range(i, n):
            if(arr[i]>arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    
    for i in range(n):
        print(arr[i],end=" ")

# bubbleSort(arr, n)


# Insertion Sort
# def insertionSort(arr, n):
#     for i in range(1, n):
#         key = arr[i]
#         j= i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1] =arr[j]
#             j= j-1
#         arr[j+1] = key

#     for i in range(n):
#         print(arr[i],end=" ")

# insertionSort(arr, n)


# Selection Sort
# def selectionSort(arr, n):
#     for i in range(n):
#         smallest = i
#         for j in range(i+1, n):
#             if(arr[smallest]>arr[j]):
#                 smallest = j
#         (arr[i], arr[smallest]) = (arr[smallest],arr[i])

#     for i in range(n):
#         print(arr[i],end=" ")

# selectionSort(arr, n)


# Heap Sort

# def heapify(arr, size, i):
#     maxIdx = i
#     left = 2*i+1
#     right = 2*i+2

#     if(left<size and arr[left]>arr[maxIdx]):
#         maxIdx = left

#     if(right<size and arr[right]>arr[maxIdx]):
#         maxIdx = right

#     if maxIdx!=i:
#         (arr[i], arr[maxIdx]) = (arr[maxIdx], arr[i])
#         heapify(arr, size, maxIdx)


# def heapSort(arr, size):
#     # Building the heapify 
#     for i in range(size//2-1, -1, -1):
#         heapify(arr, size, i)

#     # Now swaping from first and last
#     for i in range(n-1, 0, -1):
#         (arr[i], arr[0]) = (arr[0], arr[i])
#         heapify(arr, i, 0)

#     for i in range(n):
#         print(arr[i],end=" ")

# heapSort(arr, n)


# Quick Sort


# def partition(arr, low, high):
#     pivot = arr[high]
#     i=low-1
#     for j in range(low, high):
#         if(arr[j]<pivot):
#             i=i+1
#             (arr[i],arr[j]) = (arr[j], arr[i])
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#     return (i+1)


# def QuickSort(arr, low, high):
#     if(low<high):
#         pivotIdx = partition(arr, low, high)
#         QuickSort(arr, low, pivotIdx-1)
#         QuickSort(arr, pivotIdx+1, high)


# QuickSort(arr, 0, n-1)
# for i in range(n):
    # print(arr[i],end=" ")



# Merge Sort

def conquer(arr, si, midIdx, ei):
    merge = [0]*(ei-si+1)
    idx1 = si
    idx2 = midIdx+1
    x = 0
    while(idx1<=midIdx and idx2<=ei):
        if(arr[idx1]<arr[idx2]):
            merge[x] = arr[idx1]
            idx1+=1
        else:
            merge[x] = arr[idx2]
            idx2+=1
        x+=1

    while(idx1<=midIdx):
        merge[x] = arr[idx1]
        idx1+=1
        x+=1

    while(idx2<=ei):
        merge[x] = arr[idx2]
        idx2+=1
        x+=1
    
    for i in range(len(merge)):
        arr[si+i] = merge[i]


def divide(arr, si, ei):
    if(si>=ei):
        return
    
    midIdx = si+(ei-si)//2
    divide(arr, si, midIdx)
    divide(arr, midIdx+1, ei)
    conquer(arr, si, midIdx, ei)

divide(arr, 0, n-1)
for i in range(n):
    print(arr[i],end=" ")

