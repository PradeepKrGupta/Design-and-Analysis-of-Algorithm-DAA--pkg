import timeit

def selection(a,s):

    for step in range(s):

        min_idx=step

        for i in range(step+1,s):

            if a[i]<a[min_idx]:

                min_idx=i

            (a[step],a[min_idx])=(a[min_idx],a[step])

 

data= [234,234234354,656567,67567567,3453]

size = len(data)

start=timeit.default_timer()

selection(data,size)

end=timeit.default_timer()

print(f'Sorted Array in Ascending Order:{data}')

print(f'Time taken: {(end-start)*1000}')