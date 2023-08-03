#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
#

# A template for the first function that you are required to write.
def rotate(c, n):
    """ your docstring goes here """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    # Put the rest of your code for this function below.
    if 'a' <= c <= 'z':
        new_ord = ord(c) + n
        if new_ord > ord('z'):
            new_ord = new_ord - 26
    elif 'A' <= c <= 'Z':
        new_ord = ord(c) + n
        if new_ord > ord('Z'):
            new_ord = new_ord - 26
    else:
        new_ord = ord(c)
    return chr(new_ord)


#### Put your code for the encipher function below. ####

#function 2
def encipher(s, n):
    """ return a new string in which the letters in s have
        been "rotated" by n characters forward in the alphabet
    """
    if s == '':
        return ''
    else:
        encipher_rest = encipher(s[1:], n)
        return rotate(s[0], n) +  encipher_rest

# A helper function that you will use in implementing your 
# string_score function.
# You should *NOT* modify this function.
def letter_score(c):
    """ takes a single character c and returns a numeric score that 
        is based on how frequently that character appears in 
        English-language text documents.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': 
        return 0.1904
    elif c == 'e' or c == 'E': 
        return 0.1017
    elif c == 't' or c == 'T': 
        return 0.0737
    elif c == 'a' or c == 'A': 
        return 0.0661
    elif c == 'o' or c == 'O': 
        return 0.0610
    elif c == 'i' or c == 'I': 
        return 0.0562
    elif c == 'n' or c == 'N': 
        return 0.0557
    elif c == 'h' or c == 'H': 
        return 0.0542
    elif c == 's' or c == 'S': 
        return 0.0508
    elif c == 'r' or c == 'R': 
        return 0.0458
    elif c == 'd' or c == 'D': 
        return 0.0369
    elif c == 'l' or c == 'L': 
        return 0.0325
    elif c == 'u' or c == 'U': 
        return 0.0228
    elif c == 'm' or c == 'M': 
        return 0.0205
    elif c == 'c' or c == 'C': 
        return 0.0192
    elif c == 'w' or c == 'W': 
        return 0.0190
    elif c == 'f' or c == 'F': 
        return 0.0175
    elif c == 'y' or c == 'Y': 
        return 0.0165
    elif c == 'g' or c == 'G': 
        return 0.0161
    elif c == 'p' or c == 'P': 
        return 0.0131
    elif c == 'b' or c == 'B': 
        return 0.0115
    elif c == 'v' or c == 'V': 
        return 0.0088
    elif c == 'k' or c == 'K': 
        return 0.0066
    elif c == 'x' or c == 'X': 
        return 0.0014
    elif c == 'j' or c == 'J': 
        return 0.0008
    elif c == 'q' or c == 'Q': 
        return 0.0008
    elif c == 'z' or c == 'Z': 
        return 0.0005
    else:
        return 0.0

#### Put your code for string_score and decipher below. ####

# function 4
def string_score(s):
    """ return the sum of the letter score values of the 
        characters in s
    """
    lc = [letter_score(c) for c in s]
    return sum(lc)

# function 5
def decipher(s):
    """ return the original English string
    """
    options = [encipher(s, n) for n in range(26)]
    best_word = [[string_score(s), s] for s in options]
    max_pair = max(best_word)
    return max_pair[1]
    
