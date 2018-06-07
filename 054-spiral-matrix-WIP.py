"""
STATEMENT
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

EXAMPLES
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
] => [1,2,3,6,9,8,7,4,5]

"""

matrix = [
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

result = []

left=0
right=len(matrix[0])-1
top=0
bottom=len(matrix)-1

while (left <= right and top <= bottom):
    for i in range(left, right + 1):
        result.append(matrix[top][i])
    for j in range(top+1, bottom +1):
        result.append(matrix[j][right])
    for k in reversed(range(left,right)):
        if top < bottom:
            result.append(matrix[bottom][k])
    for l in reversed(range(top-1,bottom)):
        if(left < right):
            result.append(matrix[l][left])

    left=left+1
    right=right-1
    top=top+1
    bottom=bottom-1

print(result)