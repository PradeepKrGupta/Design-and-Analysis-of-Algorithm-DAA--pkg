# # Different sorting Algorithm functions
# import random
# import timeit

# # first taking array and random elements
# n = int(input("Enter the size of the array"))
# arr = []

# for i in range(n):
#     num = random.randint(1,50)
#     arr.append(num)


# # Bubble sort
# def bubbleSort(arr, n):
#     for i in range(0, n):
#         for j in range(i, n):
#             if(arr[i]>arr[j]):
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
    
#     for i in range(n):
#         print(arr[i],end=" ")

# # bubbleSort(arr, n)


# # Insertion Sort
# # def insertionSort(arr, n):
# #     for i in range(1, n):
# #         key = arr[i]
# #         j= i-1
# #         while(j>=0 and key<arr[j]):
# #             arr[j+1] =arr[j]
# #             j= j-1
# #         arr[j+1] = key

# #     for i in range(n):
# #         print(arr[i],end=" ")

# # insertionSort(arr, n)


# # Selection Sort
# # def selectionSort(arr, n):
# #     for i in range(n):
# #         smallest = i
# #         for j in range(i+1, n):
# #             if(arr[smallest]>arr[j]):
# #                 smallest = j
# #         (arr[i], arr[smallest]) = (arr[smallest],arr[i])

# #     for i in range(n):
# #         print(arr[i],end=" ")

# # selectionSort(arr, n)


# # Heap Sort

# # def heapify(arr, size, i):
# #     maxIdx = i
# #     left = 2*i+1
# #     right = 2*i+2

# #     if(left<size and arr[left]>arr[maxIdx]):
# #         maxIdx = left

# #     if(right<size and arr[right]>arr[maxIdx]):
# #         maxIdx = right

# #     if maxIdx!=i:
# #         (arr[i], arr[maxIdx]) = (arr[maxIdx], arr[i])
# #         heapify(arr, size, maxIdx)


# # def heapSort(arr, size):
# #     # Building the heapify 
# #     for i in range(size//2-1, -1, -1):
# #         heapify(arr, size, i)

# #     # Now swaping from first and last
# #     for i in range(n-1, 0, -1):
# #         (arr[i], arr[0]) = (arr[0], arr[i])
# #         heapify(arr, i, 0)

# #     for i in range(n):
# #         print(arr[i],end=" ")

# # heapSort(arr, n)


# # Quick Sort


# # def partition(arr, low, high):
# #     pivot = arr[high]
# #     i=low-1
# #     for j in range(low, high):
# #         if(arr[j]<pivot):
# #             i=i+1
# #             (arr[i],arr[j]) = (arr[j], arr[i])
# #     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
# #     return (i+1)


# # def QuickSort(arr, low, high):
# #     if(low<high):
# #         pivotIdx = partition(arr, low, high)
# #         QuickSort(arr, low, pivotIdx-1)
# #         QuickSort(arr, pivotIdx+1, high)


# # QuickSort(arr, 0, n-1)
# # for i in range(n):
#     # print(arr[i],end=" ")



# # Merge Sort

# def conquer(arr, si, midIdx, ei):
#     merge = [0]*(ei-si+1)
#     idx1 = si
#     idx2 = midIdx+1
#     x = 0
#     while(idx1<=midIdx and idx2<=ei):
#         if(arr[idx1]<arr[idx2]):
#             merge[x] = arr[idx1]
#             idx1+=1
#         else:
#             merge[x] = arr[idx2]
#             idx2+=1
#         x+=1

#     while(idx1<=midIdx):
#         merge[x] = arr[idx1]
#         idx1+=1
#         x+=1

#     while(idx2<=ei):
#         merge[x] = arr[idx2]
#         idx2+=1
#         x+=1
    
#     for i in range(len(merge)):
#         arr[si+i] = merge[i]


# def divide(arr, si, ei):
#     if(si>=ei):
#         return
    
#     midIdx = si+(ei-si)//2
#     divide(arr, si, midIdx)
#     divide(arr, midIdx+1, ei)
#     conquer(arr, si, midIdx, ei)

# divide(arr, 0, n-1)
# for i in range(n):
#     print(arr[i],end=" ")






# writing the codes 
import random 
import timeit

# n = int(input("Enter the size of the array"))
# arr = []
# for i in range(n):
#     num = random.randint(1, 50)
#     arr.append(num)


#Bubble sort
# def bubbleSort(arr, n):
#     for i in range(n):
#         for j in range(i, n):
#             if(arr[i]>arr[j]):
#                 temp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = temp
    
#     for i in range(n):
#         print(arr[i],end=" ")

# bubbleSort(arr, n)


# Insertion sort
# def insertionSort(arr, n):
#     for i in range(1, n):
#         key = arr[i]
#         j=i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1] = arr[j]
#             j=j-1
#         arr[j+1] = key

#     for i in range(n):
#         print(arr[i], end=" ")

# insertionSort(arr, n)



# Selection Sort
# def selectionSort(arr, n):
#     for i in range(0, n):
#         smallest = i
#         for j in range(i+1, n):
#             if(arr[smallest]>arr[j]):
#                 smallest = j
#         (arr[smallest], arr[i]) = (arr[i], arr[smallest])

#     for i in range(n):
#         print(arr[i], end=" ")

# selectionSort(arr, len(arr))



# heapSort 

# def heapify(arr, n, i):
#     largest = i
#     left = 2*i+1
#     right= 2*i+2

#     if(left<n and arr[left]>arr[largest]):
#         largest = left
    
#     if(right<n and arr[right]>arr[largest]):
#         largest = right

#     if largest!=i:
#         (arr[i], arr[largest]) = (arr[largest], arr[i])
#         heapify(arr, n, largest)


# def heapSort(arr, n):
#     # building the heap function
#     for i in range(n//2-1, -1, -1):
#         heapify(arr, n, i)

#     # swaping first and last
#     for i in range(n-1, 0, -1):
#         (arr[i], arr[0]) = (arr[0], arr[i])
#         heapify(arr, i, 0)

# heapSort(arr, n)
# for i in range(n):
#     print(arr[i], end=" ")   



# QuickSort
# def partition(arr, low, high):
#     pivot = arr[high]
#     i=low-1
#     for j in range(low, high):
#         if(arr[j]<pivot):
#             i=i+1
#             (arr[i], arr[j]) = (arr[j], arr[i])
    
#     (arr[i+1], arr[high]) = (arr[high], arr[i+1])
#     return (i+1)


# def QuickSort(arr, low, high):
#     if(low<high):
#         pivotIdx = partition(arr, low, high)
#         QuickSort(arr, low, pivotIdx-1)
#         QuickSort(arr, pivotIdx+1, high)


# QuickSort(arr, 0, n-1)
# for i in range(n):
#     print(arr[i], end=" ")  


# merge sort 
# def conquer(arr, si, mid, ei):
#     merge = [0]*(ei-si+1)
#     idx1 = si
#     idx2 = mid+1
#     x = 0

#     while(idx1<=mid and idx2<=ei):
#         if(arr[idx1]<=arr[idx2]):
#             merge[x] = arr[idx1]
#             idx1+=1
#         else:
#             merge[x] = arr[idx2]
#             idx2+=1
#         x+=1
        
#     while(idx1<=mid):
#         merge[x] = arr[idx1]
#         idx1+=1
#         x+=1

#     while(idx2<=ei):
#         merge[x] = arr[idx2]
#         idx2+=1
#         x+=1
    
#     for i in range(len(merge)):
#         arr[si+i] = merge[i]

# def MergeSort(arr, si, ei):
#     if(si>=ei):
#         return
#     mid = si+(ei-si)//2
#     MergeSort(arr, si, mid)
#     MergeSort(arr, mid+1, ei)
#     conquer(arr, si, mid, ei)


# MergeSort(arr, 0, n-1)
# for i in range(n):
#     print(arr[i], end=" ") 




# Bucket Sort

# def insertionSort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j= i-1
#         while(j>=0 and key<arr[j]):
#             arr[j+1] = arr[j]
#             j=j-1
#         arr[j+1] = key
#     return arr

# def BucketSort(x):
#     num_bucket = 10
#     arr=[]

#     # creating 10 buckets
#     for i in range(num_bucket):
#         arr.append([])
    
#     # putting array elements into the bucket
#     for j in x:
#         indx_buck = int(j*num_bucket)
#         arr[indx_buck].append(j)

#     # sorting them inside it
#     for i in range(num_bucket):
#         arr[i] = insertionSort(arr[i])


#     # concatinate
#     k=0
#     for i in range(num_bucket):
#         for j in range(len(arr[i])):
#             x[k] = arr[i][j]
#             k+=1
#     return x


# x = [0.897, 0.565, 0.656,
# 	0.1234, 0.665, 0.3434]
# print("Sorted Array is")
# print(BucketSort(x))





def insertionSort(arr):
    for i in range(1, len(arr)):
        key =arr[i]
        j= i-1
        while(j>=0 and key<arr[j]):
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key
    
    return arr

def BucketSort(x):
    arr = []
    num_bucket = 10

    # creating an empty buckets
    for i in range(num_bucket):
        arr.append([])

    # putting the values in empty buckets
    for j in x:
        indx_buck = int(j*num_bucket)
        arr[indx_buck].append(j)

    # sorting each of them inside it
    for i in range(num_bucket):
        arr[i] = insertionSort(arr[i])
    
    # now concatinating 
    k = 0
    for i in range(num_bucket):
        for j in range(len(arr[i])):
            x[k] = arr[i][j]
            k+=1
    return x

x = [0.456, 0.239, 0.128, 0.679, 0.358]
print("Sorted Array is")
print(BucketSort(x))