# 
# ps5pr8.py - Problem Set 5, Problem 8
#
# Processing sequences with loops
#

# Function 1
def total_len(words):
    """ return the value obtained by adding together 
        the lengths of all of the strings in the list """
    total = 0
    for i in range(len(words)):
        total += len(words[i])
    return total

# Function 2
def exclaim(s):
     """ return the string formed by adding an exclamation point """
     result = ''
     for i in s:
        result += (i + "!")
     return result
 
# Function 3
def consonants(s):
    """ return a list containing the consonants (if any) in s """ 
    result = []
    for i in s:
        if i not in 'aeiou':
            result += i
    return result

# Function 4
def smaller_of(vals1, vals2):
    """ return a new list in which each element is the the smaller of the 
        corresponding elements from the original lists """
    result = []
    len_shorter = min(len(vals1), len(vals2))
    for i in range(len_shorter):
        if vals1[i] <= vals2[i]:
            result += [vals1[i]]
        elif vals2[i] <= vals1[i]:
            result += [vals2[i]]
    return result