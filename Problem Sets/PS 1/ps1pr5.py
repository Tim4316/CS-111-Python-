#function 1
def first_and_last(values):
    """ return a new list containing the first value
        of the original list followed by the last value
        of the orignial list
    """
    first = values[0]
    last = values[-1]
    return [first, last]

#funtion 2
def longer_len(s1, s2):
    """ return the length of the longer string
    """
    if len(s1) > len(s2):
        longer_len = len(s1)
    else:
        longer_len = len(s2)
    return longer_len
      
#function 3
def move_to_end(s,n):
    """ return a new string in which the first
        n characters of s have been moved to
        the ned of the string
    """
    if n >= len(s):
        return s
    else:
        return s[n:] + s[:n]   