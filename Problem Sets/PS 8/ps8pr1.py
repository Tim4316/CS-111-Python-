#
# ps8pr1.py  (Problem Set 8, Problem 1)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        self.month = init_month
        self.day = init_day
        self.year = init_year


    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    def advance_one(self):
        """ Returns the called object so that it represents one calendar day 
            after the date that it originally represented. """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if self.is_leap_year() == True:
            days_in_month[2] = 29
          
        self.day += 1
            
        if self.day > days_in_month[self.month]:
             self.month += 1
             self.day = 1
            
        if self.month > 12:
            self.year += 1
            self.month = 1
    
    def advance_n(self, n):
        """ Changes the calling object so that it represents n calendar days after 
            the date it originally represented. """
        print(self)
        for k in range(n):
            self.advance_one()
            print(self)
            
    def __eq__(self, other):
        """ returns True if the called object (self) and the argument (other) represent 
            the same calendar date (i.e., if the have the same values for their day, month, 
            and year attributes). """
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
    
    def is_before(self, other):
        """ returns True if the called object represents a calendar date that occurs before 
            the calendar date that is represented by other. """
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        else:
            return False
    
    def is_after(self, other):
        """ returns True if the calling object represents a calendar date that occurs after the 
            calendar date that is represented by other. """
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        else:
            return False
    
    def days_between(self, other):
        """ returns an integer that represents the number of days between self and other. """
        s = self.copy()
        o = other.copy()
        num = 0
        
        if s.is_before(o) == True:
            while s.is_before(o) == True:
                s.advance_one()
                num -= 1
        else:
            while s.is_after(o) == True:
                o.advance_one()
                num += 1
        return num
    
    def day_name(self):
        """ returns a string that indicates the name of the day of the week of the Date object 
            that calls it. """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        fixed = Date(11, 8, 2021)
        between = self.days_between(fixed)
        return day_names[between]
        
        
       


    #### Put your code for problem 1 below. ####
    #### Make sure that it is indented by an appropriate amount. ####
