#Selection sort
#time complexity O(n^2)
def selectionSort(arr):
    for i in range(len(arr)):
        min = arr[i]
        loc = 1
        nextElement = i+1 #point to succesive element of index i
        for j in range(nextElement,len(arr)):
            if(arr[j] < min):
                min = arr[j]
                loc = j
            
        if(min != arr[i]):
            temp = arr[i]
            arr[i] = min
            arr[loc] = temp
    return arr

            