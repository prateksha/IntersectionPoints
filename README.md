
# <p align="center"> Design And Analysis of Algorithms <br> Project </p>

#### <p align="right"> Ayush Yadav (IMT2017009) <br> Prateksha U (IMT2017517) </p>


## Problem Statement
You are given equations of ​n​ lines as input. The equation of a line is of the form ​y=mx+c​ where ​m​ is the slope and ​c​ is the y-intercept. Design an ​O(n log n)algorithm that counts the number of intersection points that lie on the right side of the line x=0 (y-axis).

The following assumptions have been made:

- No line is parallel to the x-axis or y-axis.
- No two lines are parallel to each other.
- No three lines intersect at the same point. Hence, there are exactly ​n(n-1)/2 intersection points in the configuration.
- All the intersection points lie in the bounding box [-100,100]x[-100,100]. In other words, the x and y coordinates of any intersection point have an absolute value of atmost 100.

## Sources 
- Introduction to Algorithms by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein
- Data Structures and Algorithms course codes

## Data Structures Used
We used 2-D Array for storing [ slope, y-intecept ] input.

## Example
*Number of equations = 5*
1.  y = 2x + 3
2.  y = 5x + 0
3.  y = -4x +6
4.  y = x + 1
5.  y= -3x + 7

![alt text](/Plot.png "Plot for the Example")

Consider 2 equations .
1. y = m<sub>1</sub>x + c<sub>1</sub>
2. y = m<sub>2</sub>x + c<sub>2</sub>


Since no 2 lines are parallel to each other, Line 1 and Line 2 must intersect.

<p align ="center"> m<sub>1</sub>x + c<sub>1</sub>  = m<sub>2</sub>x + c<sub>2</sub> <br> x = (c<sub>1</sub> - c<sub>2</sub>)/(m<sub>2</sub> - m<sub>1</sub>)</p>

Since the intersection point has to lie on the right side of the line x = 0 ( y-axis ), we will consider the case where value of ‘x’ in Eq. 3 is greater > 0. 

<p align ="center"> i.e., (c<sub>1</sub> - c<sub>2</sub>)/(m<sub>2</sub> - m<sub>1</sub>) > 0 <br>

For the above equation to be true, the values of c (y-intercept) and m (slope) have to satisfy one of the following conditions:<br>
<p align = "center">
 c<sub>1</sub> > c<sub>2</sub> AND m<sub>2</sub> > m<sub>1</sub> 
 <br>
 c<sub>1</sub> < c<sub>2</sub> AND m<sub>2</sub> < m<sub>1</sub> </p>

## PSEUDO CODE

Input:  input_array consists of **n** [m,c] pairs.

~~~~
input_array.sort -> based on c values (y-intercept)
m_array = []

for 1 to n:
    m_array[i] = input_array[i][0] 

sort_and_count(m_array)
~~~~

A and B are two sorted lists. i, j are the pointers to the lists.

~~~~
merge_and_count (A, B)

    count = 0
    while (A != empty and B!= empty)
        C.append( min(A[i], B[j])
        if( B[j]<A[i] )
            count += number of elements left in A
            j++
        else
            I++
        add the remaining elements to c

    return count, C
~~~~


With merge-and-count, we can design the count inversion algorithm as follows:

~~~~
sort_and_count (C)

    if ( C has one element)
        return 0
    else
        divide C into A and B
        (c1, A) = sort_and_count (A)
        (c2, B) = sort_and_count (B)
        (c3, C) = merge_and_count(A, B)

    return c1+c2+c3, C
~~~~
## Proof Of Correctness


Consider 2 equations .
1. y = m<sub>1</sub>x + c<sub>1</sub>
2. y = m<sub>2</sub>x + c<sub>2</sub>


Since no 2 lines are parallel to each other, Line 1 and Line 2 must intersect.

<p align ="center"> m<sub>1</sub>x + c<sub>1</sub>  = m<sub>2</sub>x + c<sub>2</sub> <br> x = (c<sub>1</sub> - c<sub>2</sub>)/(m<sub>2</sub> - m<sub>1</sub>)</p>

Since the intersection point has to lie on the right side of the line x = 0 ( y-axis ), we need to consider the case where the above relation is positive.

<p align ="center"> i.e., (c<sub>1</sub> - c<sub>2</sub>)/(m<sub>2</sub> - m<sub>1</sub>) > 0 <br>

For the above equation to be true, the values of c (y-intercept) and m (slope) have to satisfy one of the following conditions:<br>
<p align = "center">
 c<sub>1</sub> > c<sub>2</sub> AND m<sub>2</sub> > m<sub>1</sub>            ---- (1)
 <br>
 c<sub>1</sub> < c<sub>2</sub> AND m<sub>2</sub> < m<sub>1</sub> ----(2)</p>


The above relation of intersection points can be reduced to a prolem of counting inversions as shown below.

Sorting the array of slopes (call this array M) (i.e., [m<sub>1</sub>, m<sub>2</sub>,m<sub>3</sub> ... m<sub>n</sub>]) on the basis of the corresponding c (y-intercept) values.

We get an array such that, ∀ i, j ∈ indices of M. 
<p align = "center"> i < j  ⇒ c<sub>i</sub> < c<sub>j</sub> ----(3)</p align = "center">
and if,
<p align = "center"> M[i] > M[j] ----(4)</p align = "center">
we can say that the point of the intersection of the two lines is beyond the x-axis (from (1) and (2)). The above relations (3) and (4) show the reduction of the intersection pairs problems into the counting inversions problem.

Hence, counting the number of inversions in the sorted M array will give us the number of intersection points beyond the x-axis.

- _**Claim 1**_ : *merge_and_count merges two given sorted arrays.*




## Analysis of Running Time

The Recurrence Relation for MergeSort is:
<p align="center" > T(n) = 2T(n/2) + n <br>
T(n) = 4T(n/4) + 2n <br>
T(n) = 8T(n/8) + 3n <br>
... <br>
T(n) = 2<sup>k</sup>T(n/2<sup>k</sup>) + kn <br>
</p>
Proof using Induction:<br>
For k=1: 
T(n) = 2T(n/2) + n is true. <br><br>

Induction hypothesis: <br>
T(n) = 2<sup>k-1</sup>T(n/2<sup>k-1</sup>) + (k-1)n <br>
T(n) = 2[2<sup>k-1</sup>T(n/2*2<sup>k-1</sup>) + (k-1)n/2] + n <br>
Hence proved, T(n) = 2<sup>k</sup>T(n/2<sup>k</sup>) + kn is true for all k. <br>

Put k = log(n):
T(n) = n(T(1)) + n log(n) = O(n log(n))

- Sorting the input based on **c** values (y-intercept) using TimSort(Default sorting algorithm in Python) - θ(n log(n))
- To count the inversions in **m** array (slopes array), the algorithm is a modified form of Merge Sort - θ(n log(n))
- Therefore the Time Complexity is θ(n log(n)) + θ(n log(n)).
<p align = "center"> Time Complexity = θ(n log(n)) </p>

## Instructions on how to run the code
- The code is written in Python. The code can be run by using the following command for a given input file (Suppose the input file name is **input1.txt**)  -  **python IntersectionPoints.py TestCases/input1.txt**
- The **generate_input.py** generates random input values for a large value of **n**. It is written to the file **large_input.txt**. The value of **n** can be changed in the code for a different set of inputs.

## Individual Contributions

- **Prateksha** : Wrote the code. Wrote the script for generating large inputs. Completed other sections of README.

- **Ayush** : Wrote the proof of correctness and running time analysis. Wrote sample test cases. Completed the README for TestCase formats.

- **Combined Contribution** : Came up with the algorithm for the question.


