def isPalindrome(self, s):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while l <r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l +=1; r -= 1
    return True


def isPalindrome(self, s):
    newS= [i.lower() for i in s if i.isalnum()]
    return newS == newS[::-1]


def isPalindrome(self, s):
        s = "".join([c.lower() for c in s if c.isalnum()])
        return s == s[::-1]

# Regex

def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    import re
    s = re.sub('[^0-9a-zA-Z]', '', s).lower()
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i + 1, j - 1
    # empty or palindrome return True
    return True