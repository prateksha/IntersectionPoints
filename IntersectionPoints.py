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


array_of_variables = []
fname = 'input.txt'
with open(fname, 'r') as f:
    no_of_lines = int(f.readline())
    for i in range(no_of_lines):
        m, c = map(int, f.readline().split())
        array_of_variables.append([m, c])
    print (array_of_variables)

# Sorting based on c
array_of_variables.sort(key=lambda p:p[1])
print(array_of_variables)

slopes_array = [0 for x in range(no_of_lines)]
for i in range(no_of_lines):
    slopes_array[i] = array_of_variables[i][0]
print(slopes_array)

sorted_array = []
for i in range(len(slopes_array)):
    sorted_array.append(0)
print (mergeSort(slopes_array, sorted_array, 0, len(slopes_array)-1))



	
