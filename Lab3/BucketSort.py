# Python3 program to sort an array
# using bucket sort


def insertionSort(arr):
	for i in range(1, len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and arr[j] > key:
			arr[j + 1] = arr[j]
			j -= 1
		arr[j + 1] = key
	return arr


def bucketSort(x):
	arr = []
	slot_num = 10 # 10 means 10 slots, each
	# slot's size is 0.1
	for i in range(slot_num):
		arr.append([])

	# Put array elements in different buckets
	for j in x:
		idx_b = int(slot_num * j)
		arr[idx_b].append(j)

	# Sort individual buckets
	for i in range(slot_num):
		arr[i] = insertionSort(arr[i])

	# concatenate the result
	k = 0
	for i in range(slot_num):
		for j in range(len(arr[i])):
			x[k] = arr[i][j]
			k += 1
	return x


# Driver Code
x = [0.897, 0.565, 0.656,
	0.1234, 0.665, 0.3434]
print("Sorted Array is")
print(bucketSort(x))

