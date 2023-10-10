# Merge Sort
# Merge sort is a divide and conquer algorithm that splits an array into equal halves, sorts them separately and then merges them. This

import random 
import timeit

n = int(input("Enter the size of the array"))
arr = []

for i in range(n):
    num = random.randint(1, 50)
    arr.append(num)


# creating the conquer function
def conquer(arr, si, mid, ei):
    merge = [0]*(ei-si+1)
    idx1 = si
    idx2 = mid+1
    x = 0
    while(idx1<=mid and idx2<=ei):
        if(arr[idx1]<=arr[idx2]):
            merge[x] = arr[idx1]
            idx1+=1
        else:
            merge[x] = arr[idx2]
            idx2+=1
        x+=1

    while(idx1<=mid):
       merge[x] = arr[idx1]
       x+=1
       idx1+=1 

    while(idx2<=ei):
       merge[x] = arr[idx2]
       x+=1
       idx2+=1 

    for i in range(len(merge)):
        arr[i+si] = merge[i]


# creating the divide function
def divide(arr, si, ei):
    if(si>=ei):
        return
    
    mid = si+(ei-si)//2
    divide(arr, si, mid)
    divide(arr, mid+1, ei)
    conquer(arr, si, mid, ei)



start = timeit.default_timer()
divide(arr, 0, n-1)
end = timeit.default_timer()
print("\n")
for i in range(n):
    print(arr[i],end=" ")

print('\n')
print("Time taken by QuickSort is :",(end-start)*1e3)