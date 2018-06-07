"""

STATEMENT
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
CLARIFICATIONS
- What happens when there is no solution? Assume solution exists.
- Can the list be empty? No.
- Is the list sorted? Not necessarily.
EXAMPLES
[2, 7, 11, 15], 9 -> [0,1]



def findSum(arr,t):
    n = len(arr)
    found = True
    for i in range (0, n-1):
        for j in range (i+1, n):
            if (arr[i] + arr[j] == t):
                print(arr[i], arr[j])
                found = True

# Driver code
arr = [0, -4, 2, -3, 4]
t = 6
findSum(arr,t)
"""

# Using dictionaries O(n) complexity

def findSum(nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            print(i)
            if nums[i] in buff_dict:
                print (buff_dict[nums[i]], i)
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

# Driver code
arr = [0, -4, 2, -3, 4]
t = -7
findSum(arr,t)

"""
def findTriplets(arr):

    n = len(arr)
    found = True
    for i in range(0, n-2):

        for j in range(i+1, n-1):

            for k in range(j+1, n):

                if (arr[i] + arr[j] + arr[k] == 0):
                    print(arr[i], arr[j], arr[k])
                    found = True


    # If no triplet with 0 sum
    # found in array
    if (found == False):
        print(" not exist ")

# Driver code
arr = [0, -4, 2, -3, 4]

findTriplets(arr)
"""