"""

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

O(n2)
def findMaxProfit(myArr):
    maxProfit=0
    currProfit=0
    for i in range (len(myArr)):
        for j in range (i,len(myArr)):
            currProfit= myArr[j] - myArr[i]
            if currProfit > maxProfit:
                maxProfit = currProfit
    print(maxProfit)

# O(n) - kdanes algorithm
"""
def findMaxProfit(myArr):
    maxProfit=0
    currProfit=0
    minPrice=9999  # put max value of int
    #print (minPrice)
    for price in myArr:
        minPrice=min(price,minPrice)
        profit=price-minPrice
        maxProfit=max(maxProfit,profit)
    print(maxProfit)
"""

def findMaxProfit(myArr):
    maxProfit=0
    totalProfit=0
    minPrice=9999  # put max value of int
    for i in range (len(myArr)):
        minPrice=min(price,minPrice)
        profit=price-minPrice
        maxProfit=max(maxProfit,profit)
    print(maxProfit)
"""
# Driver code
myArr = [7,1,5,3,6,4]
findMaxProfit(myArr)