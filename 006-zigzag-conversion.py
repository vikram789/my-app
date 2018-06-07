"""
STATEMENT
Given a string and a number of rows, pring the string in a zigzag fashion across rows.
"APPLE" can be written as the following in 3 rows:
A       E
  P   L
    P

"""
def zigzag(str,rows):

    # initialize 2 D array
    Matrix = [["" for x in range(len(str))] for y in range(rows)]

    if(rows==1):
        print(str)
        return 0

    down=True
    row_num=0
    for i in range(len(str)):
        if(i==0):
            Matrix[row_num][i]=str[i];

        else:
            if(down == True):
                row_num=row_num+1
                Matrix[row_num][i]=str[i];
                if(row_num == rows -1):
                    down=False
            else:   # Down is false to move up
                row_num=row_num-1
                Matrix[row_num][i]=str[i];
                if(row_num == 0):
                    down=True

    #   print("".join(Matrix[0]),  "".join(Matrix[1]) , "".join(Matrix[2]))
    for i in range(rows):
        print(Matrix[i])

#   print (Matrix[i in range(rows)])

# Driver Code
str="APPLEROCKS"
zigzag(list(str),4)

