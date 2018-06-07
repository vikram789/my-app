"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""

def addTwoNo(arr1,arr2):

    length=max(len(arr1),len(arr2))
    arr3=[]
    carry = 0
    for i in range (0 , length):
        sum=arr1[i] + arr2[i] + carry
        remainder=sum%10
        arr3.append(remainder)
        if  (sum > 9):
            carry=1
        else:
            carry=0
    if carry == 1:
        arr3.append(1)
    print (arr3)


#Driver code
arr1=[2 , 4 , 3]
arr2=[9 , 6 , 9]
addTwoNo(arr1,arr2)
# above solution will not work if array is diff size. to make it work, just append 0 in the end to make it equal

"""
Above problem has issue

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
# @return a ListNode
def addTwoNumbers(self, l1, l2):
    carry = 0
    root = n = ListNode(0)
    while l1 or l2 or carry:
        v1 = v2 = 0
        if l1:
            v1 = l1.val
            l1 = l1.next
        if l2:
            v2 = l2.val
            l2 = l2.next
        carry, val = divmod(v1+v2+carry, 10)
        n.next = ListNode(val)
        n = n.next
    return root.next

Time complexity : O(\max(m, n))O(max(m,n))

"""