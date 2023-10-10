import random
import timeit
n = int(input("Enter the size of the array\n"))
arr = []

for i in range(0,n):
    num = random.randint(1, 100)
    arr.append(num)

def BubbleSort(n):
    for i in range(0, n):
        for j in range(i, n):
            if arr[i]>arr[j]:
                temp = arr[i]
                arr[i]=arr[j]
                arr[j] = temp

    for i in range(0, n):
        print(arr[i],end=" ")
        

start =  timeit.default_timer()
BubbleSort(n)
end = timeit.default_timer()
print("\n")
print("Time taken to run by bubble sort is :",(end-start)*1e3)
