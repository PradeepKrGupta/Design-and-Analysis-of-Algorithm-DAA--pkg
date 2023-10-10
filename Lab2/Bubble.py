# Bubble sorting
import random 
import timeit

swaped = False
def BubbleSort(arr):
    for i in range(num-1):
        for j in range(num-i-1):
            if arr[j]>arr[j+1]:
                swaped = True
            arr[j],arr[j+1]=arr[j+1],arr[j]

        if not swaped:
            return 


num = int(input("Enter the size of array"))
arr = []
for i in range(num-1):
    arr[i] = random.randint(0, 100)

start = timeit.default_timer()
BubbleSort(arr)
end = timeit.default_timer()
execution_time = (end-start)*1e3
print('Execution Time:', execution_time,'ms')


for i in range(len(arr)):
    print("%d"%arr[i], end=" ")