#implement atoi which converts a string to an integer.
# https://leetcode.com/problems/string-to-integer-atoi/description/

import re

def atoi(str):
    print(str)
    str = str.strip()
    print(str)
    str = re.findall('(^[\+\-0]*\d+)\D*', str)
    print (str)
    try:
        result = int(''.join(str))
        MAX_INT = 2147483647
        MIN_INT = -2147483648
        if result > MAX_INT > 0:
            return MAX_INT
        elif result < MIN_INT < 0:
            return MIN_INT
        else:
            return result
    except:
        return 0

mystr="  345df asdf 344"
print(atoi(mystr))
