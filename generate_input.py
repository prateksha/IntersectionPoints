import random
# Number of Equations
n = 60

# Array to store the values of slopes
m = []
m = random.sample(range(500),n)

# Array to store the values of y-intercepts
c = []
c = random.sample(range(700),n)

# Writing the values to the file in the required input format
f = open("TestCases/large_input.txt","w+")
f.write(str(n) + "\n")

for i in range(n):
    f.write(str(m[i]) + " " + str(c[i]) + "\n")

f.close()
