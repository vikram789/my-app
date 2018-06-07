"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""
def findMax(myArr):
    currCount=myArr[0]
    MaxCount=myArr[0]
    for num in myArr[1:]:
        currCount= max(num, num + currCount)
        MaxCount = max (MaxCount, currCount)
    print (MaxCount)
# Driver Code
myArr = [-2,1,-3,4,-1,2,1,-5,4]
findMax(myArr)