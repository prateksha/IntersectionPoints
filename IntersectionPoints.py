number_of_lines = input()
# array_of_variables = [[0,0],[0,0],[0,0],[0,0],[0,0]]
array_of_variables = [[0 for x in range(2)] for y in range(number_of_lines)] 
for i in range(number_of_lines):
    m = input()
    c = input()
    array_of_variables[i][0] = m
    array_of_variables[i][1] = c

print(array_of_variables)
# Sorting based on c
array_of_variables.sort(key=lambda p:p[1])
print(array_of_variables)

slopes_array = [0 for x in range(number_of_lines)]
for i in range(number_of_lines):
    slopes_array[i] = array_of_variables[i][0]
print(slopes_array)

