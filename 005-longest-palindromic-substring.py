# This function prints the longest palindrome # substring of st[]. It also returns the length
# of the longest palindrome
# Complexity O(n^2)
def longestPalSubstr(st) :
    n = len(st) # get length of input string

    # table[i][j] will be false if substring
    # str[i..j] is not palindrome. Else
    # table[i][j] will be true
    table = [[0 for x in range(n)] for y
             in range(n)]

    # All substrings of length 1 are  # palindromes
    maxLength = 1
    i = 0
    while (i < n) :
        table[i][i] = True
        i = i + 1

    # check for sub-string of length 2.
    start = 0
    i = 0
    while i < n - 1 :
        if (st[i] == st[i + 1]) :
            table[i][i + 1] = True
            start = i
            maxLength = 2
        i = i + 1

    # Check for lengths greater than 2. k is length of substring
    k = 3
    while k <= n :
        # Fix the starting index
        i = 0
        while i < (n - k + 1) :

            # Get the ending index of substring from starting index i and length k
            j = i + k - 1

            # checking for sub-string from ith index to jth index iff st[i+1] to st[(j-1)] is a palindrome
            if (table[i + 1][j - 1] and
                    st[i] == st[j]) :
                table[i][j] = True

                if (k > maxLength) :
                    start = i
                    maxLength = k
            i = i + 1
        k = k + 1
    print "Longest palindrome substring is: ",printSubStr(st, start,
                                                          start + maxLength - 1)

    return maxLength # return length of LPS


# Driver program to test above functions
st = "forgeeksskeegfor"
l = longestPalSubstr(st)
print "Length is:", l

"""
def longestPalindrome(self, s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        tmp = self.helper(s, i, i)
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = self.helper(s, i, i+1)
        if len(tmp) > len(res):
            res = tmp
    return res
 
# get the longest palindrome, l, r are the middle indexes   
# from inner to outer
def helper(self, s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1; r += 1
    return s[l+1:r]
"""