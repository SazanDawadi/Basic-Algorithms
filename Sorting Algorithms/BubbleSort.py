#Bubble sort fxn
def bubbleSort(arr):
    for i in arr:
        for j in arr:
            if(arr[i]<arr[j]):
                # swapping if the elements is greater than bubble element
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp