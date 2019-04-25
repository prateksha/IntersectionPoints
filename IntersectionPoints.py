from sys import argv

# Function for sort_and_count. It returns the total number of invesions.
def sort_and_count(array, sortedArray, left, right):
    mid = (left + right)/2
    inversions = 0
    if (right >left):
        # Counts inversions from the left sub-array.
        inversions = sort_and_count(array, sortedArray, left, mid)
       
        # Counts inversions from the right sub-array.
        inversions += sort_and_count(array, sortedArray, mid+1, right)
        
        # Counts inversions from across the 2 arrays.
        inversions += merge_and_count(array, sortedArray, left, right, mid+1)
    return inversions

# Function for merging 2 sorted arrays. It returns the number of inversions across the 2 arrays.
def merge_and_count(array, sortedArray, left, right, mid):
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

# 2-D array that stores the [m,c] pairs.
input_array = []

script, fname = argv

with open(fname, 'r') as f:
    no_of_lines = int(f.readline())
    for i in range(no_of_lines):
        m, c = map(int, f.readline().split())
        input_array.append([m, c])

# Sorting based on c values.
input_array.sort(key=lambda p:p[1])

# Stores the slope values.
m_array = [0 for x in range(no_of_lines)]
for i in range(no_of_lines):
    m_array[i] = input_array[i][0]

# sorted_array stores the final sorted m-array after counting inversions.
sorted_array = []
for i in range(len(m_array)):
    sorted_array.append(0)
print (sort_and_count(m_array, sorted_array, 0, len(m_array)-1))



	
