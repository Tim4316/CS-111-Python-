#
# ps7pr4.py  (Problem Set 7, Problem 4)
#
# Creating a simple database program using file processing  
#
# Computer Science 111
# 

def get_city(file, city, acro):
    """ return all records in the file for the city/state combination entered 
        by the user, and output the year, rank, and population from each matching record """
    file = open(file, 'r')
    count = 0
    for line in file:
        line = line[:-1]
        fields = line.split(',')
        if  fields[2] == city and fields[3] == acro:
            pop = float(fields[-1]) * 1000
            pop = int(pop)
            print(fields[0] + ' \t' + fields[1] + '\t' + format(pop,'10,d'))
            count += 1
    if count == 0:
        print('no results found for', city + ',', acro)
    file.close()
    
def main():
    """ start the program. This function should not take any inputs, 
        and it should not return a value. """
    file = input('Enter the name of data file: ')
    
    while True:
        city = input('city:')
        if city == 'quit':
            break
        acro = input("state abbreviation: ")
        print()
        
        get_city(file, city, acro)
