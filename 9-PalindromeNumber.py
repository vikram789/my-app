"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
"""

def isPalindrome(self, x):
    if x < 0:
        return False
    p, res = x, 0
    while p:
        res = res * 10 + p % 10
        p /= 10
    return res == x


