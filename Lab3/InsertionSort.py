import timeit
import random

n = int(input("Enter the size of the number"))
arr = []
for i in range(0, n):
    num = random.randint(0, 100)
    arr.append(num)

def InsertionSort(n):
    for i in range(1, n):
        key = arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j=j-1
        arr[j+1] = key
    
    for i in range(n):
        print(arr[i],end=" ")

start = timeit.default_timer()
InsertionSort(n)
end = timeit.default_timer()

total = (end-start)*1e3
print("Total time taken by insertion sort :",total)