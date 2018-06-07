"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.
Example:

Input: 5
Output:
[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]
"""

def pascals(numrows):

    triangle = []
    rows = []
    for i in range (numrows):
        # initialize rows array
        rows = [None for _ in range(i+1)]
        rows[0] = 1
        rows[-1] = 1
        for j in range (1,len(rows)-1):
            rows[j] = triangle[i-1][j]+triangle[i-1][j-1]
        triangle.append(rows)

    print(triangle)

pascals(5)
