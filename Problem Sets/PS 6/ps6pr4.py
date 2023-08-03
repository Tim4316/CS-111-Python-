#
# ps6pr4.py (Problem Set 6, Problem 4)
#
# TT Securities    
#
# Computer Science 111
#

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
    print('(3) Find the average price')
    print('(4) Find the max price and its day')
    print('(5) Find the min single-day change and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

def avg_price(prices):
    """ returns the average price """
    result = 0
    for i in range(len(prices)):
        result += prices[i]
    avg = result / len(prices)
    return avg
        
def max_day(prices):
    """ returns the day (i.e., the index) of the maximum price """
    max_d = prices[0]
    result = 0
    for i in range(len(prices)):
        if prices[i] > max_d:
           max_d = prices[i]
    for i in range(len(prices)):
        if prices[i] == max_d:
            return result
        else:
            result += 1

def min_change_day(prices):
    """ returns the day (i.e., the index) of the minimum single-day 
        absolute change in price """
    c = abs(prices[1] - prices[0])
    result = 0
    for i in range(len(prices)):
        if i == 0:
            change = prices[i + 1] - prices[i]
        else:
            change = prices[i] - prices[i-1]
            if abs(change) < abs(c):
                c = abs(change)
    for i in range(len(prices)):
        if i == 0:
            change = abs(prices[i + 1] - prices[i])
        elif abs(prices[i] - prices[i-1]) == c:
            return result + 1
        else:
            result += 1

def any_above(prices, n):
    """ determine if there are any prices above that threshold """
    for i in range(len(prices)):
        if n < prices[i]:
            return True
    return False

def find_tts(prices):
    """ return a list containing three integers """
    max_diff = abs(prices[0] - prices[0])
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if prices[j] - prices[i] > 0 and abs(prices[i] - prices[j]) > max_diff:
                max_diff = abs(prices[i] - prices[j])
    for i in range(len(prices)):
        for j in range(i, len(prices)):
            if abs(prices[i] - prices[j]) == max_diff:
                return [i, j] + [max_diff]
    

def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        elif choice == 3:
            average = avg_price(prices)
            print('The average price is', average)
        elif choice == 4:
            max_d = max_day(prices)
            print('The max price is', prices[max_d], 'on day', max_d)
        elif choice == 5:
            min_change = min_change_day(prices)
            print('The minimum single-day change occurs on day', min_change)
            print('when the price goes from', prices[min_change - 1], 'to', prices[min_change])
        elif choice == 6:
            threshold = int(input('Enter the threshold:'))
            t_any_above = any_above(prices, threshold)
            if t_any_above == True:
                print('There is at least one price above', threshold)
            else:
                print('There are no prices above', threshold)
        elif choice == 7:
            tts = find_tts(prices)
            print('Buy on day', tts[0], 'at price', prices[tts[0]])
            print('Sell on day', tts[1], 'at price', prices[tts[1]])
            print('Total profit:', tts[-1])
        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
