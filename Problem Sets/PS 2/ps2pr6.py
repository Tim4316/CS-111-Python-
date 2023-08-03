# 
# ps2pr6.py - Problem Set 2, Problem 6
#
# Problem 6: Fun with recursion, part 3
#

# function 1
def letter_score(letter):
    """ returns the value of that letter as a 
        scrabble letter
    """
    assert(len(letter) == 1)
    if letter in ['a', 'e', 'i', 'l', 'n', 'o', 'r', 's', 't', 'u']:
        return 1
    elif letter in ['d', 'g',]:
        return 2
    elif letter in ['b', 'c', 'm', 'p']:
        return 3
    elif letter in ['f', 'h', 'v', 'w', 'y']:
        return 4
    elif letter in ['k']:
        return 5
    elif letter in ['j', 'x']:
        return 8
    elif letter in ['q', 'z']:
        return 10
    else:
        return 0

# function 2 
def scrabble_score(word):
    """ return the scrabble score of that string, the
        sum of the scrablle scores of its letter
    """
    if word == '':
        return 0
    else:
        score_in_rest = scrabble_score(word[1:])
        return letter_score(word[0]) + score_in_rest

    
# function 3 (can't figure out with extras)
def smaller_of(vals1, vals2):
    """ returns a new list in which each element is the
        smaller of the corresponding elements from the
        original lists
    """
    if (vals1 == []) or (vals2 == []):
        return []
    else:
        smaller_of_rest = smaller_of(vals1[1:], vals2[1:])
        if vals1[0] >= vals2[0]:
            return [vals2[0]] + smaller_of_rest 
        else:
            return [vals1[0]] + smaller_of_rest

# function 4 (don't know the second base case)
def merge(s1, s2):
    """ return a new string that is formed by "merging"
        together the characters in the string
        s1 and s2 to create a single string
    """
    if (s1 == '') and (s2 == ''):
        return ''
    elif (s1 == ''):
        return s2
    elif (s2 == ''):
        return s1
    else:
        merge_rest = merge(s1[1:], s2[1:])
        if s1[0] == s2[0]:
            return s1[0] + merge_rest
        else:
            return s1[0] + s2[0] + merge_rest
           
                    
                    
