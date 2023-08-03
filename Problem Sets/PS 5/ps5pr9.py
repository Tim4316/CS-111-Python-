# 
# ps5pr9.py - Problem Set 5, Problem 9
#
# Choosing the correct type of loop
#

# Function 1
def add_odds(n):
    """ return the sum of the first n positive odd integers """
    result = 0
    s = 1
    for i in range(n):
        print(result, '+', s, '=', result + s)
        result += s
        s += 2
    return result
                
        
def largest_pow2(n):
    """ return the largest power of 2 that is less than or equal to n """
    result = 0
    num = 2
    while num < n:
        num = 2
        print(num, '**', result, '=', num ** result)
        num **= result
        result += 1
    if num > n:
        num = num // 2 
    return num

