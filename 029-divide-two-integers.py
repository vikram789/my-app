
"""
STATEMENT
Divide two integers without using multiplication, division and mod operator.

EXAMPLES
34/3 -> 11
"""
def intDivide(int1,int2):
    remainder=int1
    result=0
    while(remainder >= 0):
        remainder=remainder-int2
        if(remainder >= 0):
            result=result+1
    print(result)



#Driver code
int1=44
int2=11
intDivide(int1,int2)