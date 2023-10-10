# # Bubble sort
# import random
# import timeit

# n = int(input("Enter the size of the array"))
# arr = []

# for i in range(0, n):
#     num = random.randint(1, 100)
#     arr.append(num)


# def bubbleSort(n):
#     for i in range(0, n):
#         for j in range(i, n):
#             if(arr[i]>arr[j]):
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
    
#     for i in range(0, n):
#         print(arr[i],end=" ")

# start = timeit.default_timer()
# bubbleSort(n)
# end = timeit.default_timer()
# print("\n")
# print("Time taken by bubble sort is ",(end-start)*1e3)

    


# Insertion Sorting

# import random
# import timeit

# n = int(input("Enter the size of the array"))
# arr = []

# for i in range(0, n):
#     num = random.randint(1, 100)
#     arr.append(num)

# def insertionSort(n):
#     for i in range(1, n):
#         key = arr[i]
#         j= i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1] = arr[j]
#             j=j-1
#         arr[j+1] = key
    
#     for i in range(0, n):
#         print(arr[i],end=" ")

# start = timeit.default_timer()
# insertionSort(n)
# end = timeit.default_timer()
# print("Time it will take to : ",(end-start)*1e3)



# Selection Sorting
# import random
# import timeit

# n = int(input("Enter the size of the array"))
# arr = []

# for i in range(0, n):
#     num = random.randint(1, 100)
#     arr.append(num)


# def selectionSort(n):
#     for i in range(n):
#         smallest = i
#         for j in range(i+1, n):
#             if(arr[smallest]>arr[j]):
#                 smallest=j
#         (arr[i], arr[smallest]) = (arr[smallest], arr[i])
    
#     for i in range(n):
#         print(arr[i], end=" ")



# start = timeit.default_timer()
# selectionSort(n)
# end = timeit.default_timer()
# print("Time it will take to : ",(end-start)*1e3)




# Heap Sort using heapify method

# import random
# import timeit

# size = int(input("Enter the size of the array"))
# arr = []

# for i in range(size):
#     num = random.randint(1, 50)
#     arr.append(num)


# # creating the heapify method
# def heapify(arr, size, i):
#     maxIdx = i
#     left = 2*i+1
#     right = 2*i+2
#     if (left < size and arr[left]> arr[maxIdx]):
#         maxIdx = left
    
#     if (right<size and arr[right] > arr[maxIdx]):
#         maxIdx = right

#     if maxIdx!=i:
#         (arr[i],arr[maxIdx]) = (arr[maxIdx], arr[i])
#         heapify(arr, size , maxIdx)

# def heapSort(arr, size):
#     # Building an maxheap
#     for i in range(size//2-1, -1, -1):
#         heapify(arr, size, i)

#     # pushing the first element to last
#     for i in range(size-1, 0, -1):
#         (arr[i], arr[0]) = (arr[0], arr[i])
#         heapify(arr, i, 0)

# start = timeit.default_timer()
# heapSort(arr, size)

# print('Sorted Array is array is :\n')
# for i in range(size):
#     print(arr[i], end=" ")
# end = timeit.default_timer()
# print("\n")
# print("Time taken by heapSort is :",(end-start)*1e3)




# Quick Sort

# import random
# import timeit

# n = int(input("Enter the size of the array"))
# arr = []

# for i in range(n):
#     num = random.randint(1, 50)
#     arr.append(num)

# # creating the partition function
# def partition(arr, low, high):
#     pivot = arr[high]
#     i= low-1
#     for j in range(low, high):
#         if(arr[j]<pivot):
#             i=i+1
#             (arr[i], arr[j]) = (arr[j], arr[i])
    
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#     return (i+1)

# #creating the QuickSort function
# def QuickSort(arr, low, high):
#     if(low<high):
#         pivotIdx = partition(arr, low, high)
#         # now from lwo to pivotIdx-1
#         QuickSort(arr, low, pivotIdx-1)
#         QuickSort(arr, pivotIdx+1, high)


# start = timeit.default_timer()
# QuickSort(arr, 0, n-1)
# end = timeit.default_timer()
# print("\n")
# for i in range(n):
#     print(arr[i],end=" ")

# print('\n')
# print("Time taken by QuickSort is :",(end-start)*1e3)



# merge sort
# import random 
# import timeit

# n = int(input("Enter the size of the array"))
# arr = []

# for i in range(n):
#     num = random.randint(1, 50)
#     arr.append(num)


# # now creating the conquer function
# def conquer(arr, si, mid, ei):
#     merge = [0] *(ei-si+1)
#     idx1 = si
#     idx2 = mid+1
#     x = 0
#     while(idx1<=mid and idx2<=ei):
#         if(arr[idx1]<=arr[idx2]):
#             merge[x] = arr[idx1]
#             idx1 +=1
#         else:
#             merge[x] = arr[idx2]
#             idx2+=1
#         x+=1

#     while(idx1<=mid):
#         merge[x] = arr[idx1]
#         idx1 +=1
#         x+=1
    
#     while(idx2<=ei):
#         merge[x] = arr[idx2]
#         idx2 +=1
#         x+=1
    
#     for i in range(len(merge)):
#         arr[si+i] = merge[i]



# # creating divideFunction
# def divide(arr, si, ei):
#     if(si>=ei):
#         return
#     mid = si+(ei-si)//2
#     divide(arr, si, mid)
#     divide(arr, mid+1, ei)
#     conquer(arr, si, mid, ei)


# start = timeit.default_timer()
# divide(arr, 0, n-1)
# end = timeit.default_timer()
# for i in range(n):
#     print(arr[i], end=" ")

# print("\n")
# print("Time taken by merge sort",(end-start)*1e3)