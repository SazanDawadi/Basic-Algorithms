from BubbleSort import bubbleSort
from SelectionSort import selectionSort

toBeSortedList  = [3,2,6,8,6,4,9,5]
print(f"Unsorted list \n {toBeSortedList}")
sortedList = selectionSort(toBeSortedList)

print(f"Sorted list \n {sortedList}")