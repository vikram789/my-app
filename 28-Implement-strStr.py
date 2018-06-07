"""
mplement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

"""

def findNeedle(haystack,needle):
    for i in range (0,len(haystack)-len(needle)):
        if haystack[i:i+len(needle)] == needle:
            print("Success")
            return True
        else:
            print("Failure")
            return False
#   print (myList)
# Driver code
haystack = "aaaaa"
needle = "ll"
findNeedle(haystack,needle)
