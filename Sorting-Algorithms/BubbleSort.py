#Bubble sort fxn
#time complexity O(n^2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if(arr[j]>arr[j+1]):
                # swapping if the elements is greater than bubble element
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr
