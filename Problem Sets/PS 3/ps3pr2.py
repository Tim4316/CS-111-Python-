# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
#

#function 1
def cube_all_lc(values):
    """ return a list conataing the cubes of the 
        numbeers in values
    """
    lc = [x**3 for x in values]
    return lc

#function 2
def cube_all_rec(values):
    """ return a list conataing the cubes of the 
        numbeers in values
    """
    if values == []:
        return []
    else:
        rest_cube_all_rec = cube_all_rec(values[1:])
        if values[0]:
            return [values[0] ** 3] + rest_cube_all_rec
        else:
            return  rest_cube_all_rec
        
#function 3
def consonants(s):
    """ return a list containing the consonants in s
    """
    lc = [x for x in s if x not in ['a', 'e', 'i', 'o', 'u']]
    return lc

#function 4
def num_consonants(s):
    """ return the number of consonants in s
    """
    lc = [1 for x in s if x not in ['a', 'e', 'i', 'o', 'u']]
    return len(lc)

#function 5
def most_consonants(wordlist):
    """ returns the word in the list with the most
        consonants
    """
    scored_words = [[num_consonants(x), x] for x in wordlist]
    bestpair = max(scored_words)
    return bestpair[1]
   
    