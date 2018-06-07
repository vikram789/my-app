"""
STATEMENT
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all the unique triplets.

EXAMPLES
[-1, 0, 1, 2, -1, -4] ->
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
def findTriplets(myarray):
    for i in range (len(myarray)):
        for j in range(i+1,len(myarray)-3):
            for k in range (j+1,len(myarray)):
                if ((myarray[i] + myarray[j] + myarray[k]) == 0):
                    print (myarray[i], myarray[j], myarray[k])

# Driver Code
myarray = [-1, 0, 1, 2, -1, -4]
findTriplets(myarray)