#sorting

#bubble sort
def sort_with_bubbles(lst):
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False

        for i in range(len(lst) - 1):

            if lst[i] > lst[i + 1]:
                lst[i],lst[i+1] = lst[i+1],lst[i]
                swap_occurred=True
            i=i+1
    return lst

print(sort_with_bubbles([5, 3, 1, 2, 4]))

#selection sort
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            if array[i] < array[min_idx]:
                min_idx = i
         
        (array[step], array[min_idx]) = (array[min_idx], array[step])

data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)

