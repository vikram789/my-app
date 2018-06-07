"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

"""

def removeDuplicate(myList):
    if len(myList) == 0:
        return 0
    if len(myList)== 1:
        return 1
    i = 0
    j = 1
    while  j < len(myList):
        if myList[i] == myList[j]:
            j = j+1
        else:
            i = i+1
            myList[i] = myList[j]
            j = j +1
    print (i)
#   print (myList)
# Driver code
myList=[0,0,1,1,1,2,2,3,3,4]
removeDuplicate(myList)
