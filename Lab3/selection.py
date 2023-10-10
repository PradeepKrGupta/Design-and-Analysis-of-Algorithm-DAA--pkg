
import timeit
import random
n = int(input("Enter the size of the array\n"))

arr = []

for i in range(0, n):
    num = random.randint(0,100)
    arr.append(num)

def SelectionSort(n):
    for i in range(0, n):
        smallest = i
        for j in range(i+1, n):
            if arr[smallest] > arr[j]:
                smallest = j
        (arr[i],arr[smallest])=(arr[smallest],arr[i])
    
    for i in range(0, n):
        print(arr[i],end=" ")

start = timeit.default_timer()
SelectionSort(n)
end = timeit.default_timer()

print("\n")
Total_time= (end-start)*1e3
print("Total time taken for selection sort:",Total_time)