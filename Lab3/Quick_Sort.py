# Quick Sort
import random 
import timeit


n = int(input("Enter the size of the array"))
arr = []

for i in range(n):
    num = random.randint(1, 50)
    arr.append(num)

# Now creating the partition function
def partition(arr, low, high):
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if(arr[j]<pivot):
            i=i+1
            # Swaping elements of array to put them on correct position
            (arr[i],arr[j])=(arr[j],arr[i])
    
    # Now swaping the pivot element with the greater element specified
    (arr[i+1], arr[high]) = (arr[high], arr[i+1])
    return (i+1)


# creating the QuickSort function
def QuickSort(arr, low, high):
    if(low<high):
        pivotIdx = partition(arr, low, high)

        # Now we first check from low to pivotidx to one side
        QuickSort(arr, low, pivotIdx-1)

        # Now from pivotIdx to high
        QuickSort(arr, pivotIdx+1, high)



# Now finding the time and sorted array
start = timeit.default_timer()
QuickSort(arr, 0, n-1)
end = timeit.default_timer()
print("\n Sorted array :")
for i in range(n):
    print(arr[i], end=" ")

print("\n")
print("Time taken by Quick sort is :",(end-start)*1e3)