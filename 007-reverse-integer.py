"""
STATEMENT
Reverse digits of an integer.


def reverse(myint):
    # check if int is neg or pos
    if (myint < 0):
        sign=-1
    else:
        sign=1
    # Reverse the integer
    myint=abs(myint)
    myint_rev=int(str(myint)[::-1])
    #put the sign back
    ## Add this for overflow condition (myint_rev < 2**31)
    print (myint_rev*sign)

# Python program to reverse a number



#Driver code
myint=-12345
print (myint)
reverse(myint)

"""
n = 1234
rev = 0
# print (int(n/10))
while(n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = int(n / 10)
print(rev)
