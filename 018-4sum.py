"""
STATEMENT
Given an array S integers and a target, find all unique quadruplets a, b, c, and d in S such that a + b + c + d = target.
EXAMPLES
[1, 0, -1, 0, -2, 2], 0 =>
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

def findTriplets(myarray,mysum):
    for i in range (len(myarray)):
        for j in range(i+1,len(myarray)-3):
            for k in range (j+1,len(myarray)-2):
                for l in range (k+1,len(myarray)):
                    if ((myarray[i] + myarray[j] + myarray[k] + myarray[l]) == mysum):
                        print (myarray[i], myarray[j], myarray[k], myarray[l])

# Driver Code
myarray = [1, 0, -1, 0, -2, 2]
mysum=0
findTriplets(myarray,mysum)


