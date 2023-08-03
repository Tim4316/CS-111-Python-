# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

#function 1
def cube(x):
    """returns the opposite of its input
    """
    return x**3

#function 2
def convert_to_inches(yards, feet):
    """returns the corresponding 
        lenght to inches
    """
    if feet < 0:
        feet = 0
    if yards < 0:
        yards = 0
    length = (feet * 12) + (yards * 36)
    return length

#function 3
def area_sq_inches(height_yds, height_ft, width_yds, width_ft):
    """return the area of the rectangle 
        in square inches
    """
    height = convert_to_inches(height_yds, height_ft)
    width = convert_to_inches(width_yds, width_ft)
    area = height * width
    return area

#function 4
def median(a, b, c):
    """return the median of the three inputs
    """
    if (c >= a >= b) or (b >= a >= c):
        median = a
    if (c >= b >= a) or (a >= b >= c):
        median = b
    if (a >= c >= b) or (b >= c >= a):
        median = c
    return median
    

 