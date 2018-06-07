"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
([(]))
"""

class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
    
class Solution:
    def checkValidity(self, mystr):

        myList=list(mystr)
        print (myList)
        workList=[]
        for i in (0,len(myList)-1):
            if len(workList)==0:
                workList.append(myList[i])
            else:
                if myList[i] == "{|[|(":
                    workList.append(myList[i])
                else:
                    if  workList[len(workList)-1] == "(":
                        matchchar=")"
                    else:
                        if workList[len(workList)-1] == "[":
                            matchchar="]"
                        else:
                            if workList[len(workList)-1] == "{":
                                matchchar="}"
                    if matchchar == myList[i]:
                        workList.pop()
        print(workList)
        if len(workList) == 0:
            print("true")
        else:
            print("false")



# Driver code
mystr="{[}]}"
myobjectx = Solution()
myobjectx.checkValidity(mystr)
