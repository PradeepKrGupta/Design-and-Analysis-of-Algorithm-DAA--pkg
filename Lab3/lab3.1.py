import random
import timeit
a=[]
for i in range(1,999):
    a.append(random.randint(0,10000))
times=[]

def merge_sort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        merge_sort(L)
        merge_sort(M)

        i = j = k = 0

        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i =i+1 
            else:
                array[k] = M[j]
                j =j + 1
            k =k+ 1

        while i < len(L):
            array[k] = L[i]
            i =i+1 
            k =k+ 1

        while j < len(M):
            array[k] = M[j]
            j =j + 1
            k =k+ 1

b=a
start=timeit.default_timer()
merge_sort(b)
end=timeit.default_timer()

merge=((end-start)*1000)
print("Sorted array is\n: ",b)

print(f'Time taken by using merge sort: {merge} ms\n')
times.append(merge)


#Quick Sort
def partition(array, low, high):

  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])

  return i + 1

def quick_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)

b=a
size = len(b)

start=timeit.default_timer()
quick_sort(b, 0, size - 1)
end=timeit.default_timer()

quick=((end-start)*1000)
print("Sorted array is\n: ",b)

print(f'Time taken by using quick sort: {quick} ms\n')
times.append(quick)

#Bucket Sort

def bucket_sort(array):
    bucket = []

    for i in range(len(array)):
        bucket.append([])

    for j in array:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

b=a

start=timeit.default_timer()
print("Sorted array is\n:")
print(bucket_sort(b))
end=timeit.default_timer()

bucket=((end-start)*1000)
print(f'Time taken by using bucket sort: {bucket} ms\n')
times.append(bucket)
