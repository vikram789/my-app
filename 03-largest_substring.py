"""
Given a string, find the length of the longest substring without repeating characters.
convert string into list

curr_str =[]
largest_str = []

for all chars over the list, break if

curr_str.append(str[i]

if str[i] == str[i+1]
    if curr_str. > largst_str
        largst_str=curr_str.
    # zero the current string
    curr_str = []


largst_str

if len(curr_str)




def findLarg(str1):
    curr_str =[]
    largest_str = []
    input_str=list(str1)

    for i in range (0,len(input_str)):
        curr_str.append(input_str[i])
        if (i < len(input_str)-1):
                if (input_str[i] == input_str[i+1]):
                    if(len(curr_str) > len(largest_str)):
                        largest_str=curr_str
                        curr_str =[]
        else:
            if(len(curr_str) > len(largest_str)):
                largest_str=curr_str
                curr_str =[]
    substr=''.join(largest_str)
    print (substr)

# Driver Code
str1 = 'vikrramasdafgfdsdfghsdfsfgg'
findLarg(str1)



    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and start <= usedChar[s[i]]:
                start = usedChar[s[i]] + 1
            else:
                maxLength = max(maxLength, i - start + 1)

            usedChar[s[i]] = i

        return maxLength

"""

def lenStr(mystr):
    maxLength = 0
    usedChar = []
   # currLength = 0
    for i in range(len(mystr)):
        if mystr[i] in usedChar:
           # currLength = 0
            usedChar = []
        else:
           # currLength = +1
           usedChar.append(mystr[i])
        maxLength = max(maxLength,len(usedChar))
    print(maxLength)

# Driver Code
str1 = 'pwwkew'
lenStr(str1)

# Time : O(n)
# Space : O(2n)


