#insertion sort

def sort_with_select(a_list):
    for i in range(len(a_list)):
        minIndex = i
        for j in range(i + 1, len(a_list)):
            if a_list[j]<a_list[minIndex]:  
                minIndex = j  
        minValue = a_list[minIndex]
        del a_list[minIndex]
        a_list.insert(i, minValue)
    return a_list

print(sort_with_select([5, 3, 1, 2, 4]))


#merge sort
def mergeSort(array):
    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        M = array[r:]

        mergeSort(L)
        mergeSort(M)

        i = j = k = 0


        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = M[j]
                j += 1
            k += 1


        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            array[k] = M[j]
            j += 1
            k += 1

def printList(array):
    for i in range(len(array)):
        print(array[i], end=" ")
    print()


if __name__ == '__main__':
    array = [6, 5, 12, 10, 9, 1]

    mergeSort(array)

    print("Sorted array is: ")
    printList(array)
    
    