"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]

Input: [9,9,9]
Output: [1,0,0,0]

Explanation: The array represents the integer 123.
"""

def findOP(myArr):

    carry = 0

    for i in reversed(range(0,len(myArr))):
        if myArr[i] < 9 and carry == 0:
            myArr[i]+=1
            print(myArr)
            return True
        elif myArr[i] < 9 and carry == 1:
            myArr[i]+=carry
            print(myArr)
            return True
        else:
            myArr[i] = 0
            carry = 1



# Driver code
myArr=  [8,9,9]
findOP(myArr)

"""
def findOP(myArr):

    myStr = ''.join(str(x) for x in myArr)
    print(myStr)
    myInt=int(myStr)+1
    print(myInt)



# Driver code
myArr=  [8,9,9]
findOP(myArr)
"""