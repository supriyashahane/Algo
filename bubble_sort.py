def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            print arr[i],
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
arr = [64,34,25,12,22,11,90]
print arr,
bubbleSort(arr)
print "sorted arr is:"
for i in range(len(arr)):
    print arr[i],
