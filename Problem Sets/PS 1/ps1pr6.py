#function 1
def mirror(s):
    """ return a mirrored version of s that is
        twice the length of the original string
    """
    value = s[:] + s[::-1]
    return value

#function 2
def ends_match(s):
    """ return True if the first character in s
        matches the last charcter in s, and
        False otherwise
    """
    if s[0] == s[-1]:
        value = True
    else:
        value = False
    return value

#function 3
def replace_end(values, new_end_vals):
    """ return a new list in which the elements in
        new_end_vals have replaced the last n elements
        of the list values, where n is the length of
        new_end_vals
    """
    n = len(new_end_vals)
    s = values
    if n >= len(s):
        return(new_end_vals)
    else:
        return values[0:-n] + new_end_vals[:]



#function 4
def repeat_elem(values, index, num_times):
    """ return a new list in which the element 
        of values at position index has been 
        repeated num_times times
    """
    s = values[:index] +  [values[index]] * num_times + values[index + 1:]
    return s

      

        