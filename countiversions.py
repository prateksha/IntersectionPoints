def mergeSort(array, sortedArray, left, right):
    mid = (left + right)/2
    inversions = 0
    if (right >left):
        inversions = mergeSort(array, sortedArray, left, mid)
        inversions += mergeSort(array, sortedArray, mid+1, right)
        inversions += merge(array, sortedArray, left, right, mid+1)
    return inversions



def merge(array, sortedArray, left, right, mid):
    inversions = 0
    i = left
    j = mid
    k = left
    while (i < mid  and j <= right):
        if (array[i] <= array[j]):
            sortedArray[k] = array[i]
            i += 1
            k += 1
        else :
            sortedArray[k] = array[j]
            inversions += (mid - i)
            j += 1
            k += 1 
    while (i < mid):
        sortedArray[k] = array[i]
        i += 1
        k += 1
    while (j <= right):
        sortedArray[k] = array[j]
        j += 1
        k += 1 
    i = left
    while(i <= right):
        array[i] = sortedArray[i]
        i+=1

    return inversions

inp = [1,3,9,6,8,4]
length = len(inp)
sort = []
for i in range(len(inp)):
    sort.append(0)
print (mergeSort(inp, sort, 0, len(inp)-1))