"""
STATEMENT
Write a function to find the longest common prefix string amongst an array of strings.

EXAMPLES
["ab", "a", "acd", "aaa"] -> "a"
"""

def findPrefix(mystr):
    print (mystr[0][0])
    for i in range(len(mystr[0])):
        # print (i)
        for s in mystr[1:]:
            #   print(s)
            if(len(s) <= i or s[i] != mystr[0][i]):
                print (mystr[0][:i])
                return 0



#Driver code
mystr=["abcxxx", "abc", "abc", "abc"]
findPrefix(mystr)