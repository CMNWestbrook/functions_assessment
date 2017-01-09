"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declarations - Part 1 questions aren't
included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

    >>> calculate_price(25, "CA")
    27.0

    >>> calculate_price(400, "NM")
    420.0

    >>> calculate_price(150, "OR", 0)
    150

    >>> calculate_price(60, "PA")
    65.0

    >>> calculate_price(38, "MA")
    40.9

    >>> calculate_price(126, "MA")
    135.3

PART THREE: Write your own function declarations - Part 3 questions aren't
included in the doctest.

"""

###############################################################################

# PART ONE

# NOTE: We haven't given you function signatures or docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


#    (a) Write a function that takes a town name as a string and evaluates to
#        `True` if it is your hometown, and `False` otherwise.


def where_i_am_from(hometown):
    """this is true if the value passed in is my specific hometown with the correct
    capitilization. this is false in all other cases.

    """
    if hometown == "Daly City":
        return True
    else:
        return False

#    (b) Write a function that takes a first and last name as arguments and
#        returns the concatenation of the two names in one string.


def full_name(first_name, last_name):
    """returns passed in values for a first and last name and returning them 
    as a string with a space between each part of the name.
    """
    return first_name + " " + last_name


#    (c) Write a function that takes a home town, a first name, and a last name
#        as arguments, calls both functions from part (a) and (b) and prints
#        "Hi, 'full name here', we're from the same place!", or "Hi 'full name
#        here', where are you from?" depending on what the function from part
#        (a) evaluates to.


def name_and_origin_greeting(hometown, first_name, last_name):
    """ this function takes arguments of first name, last name, and hometown.
    If the hometown is the same or different as the from the where_i_am_from 
    function it prints one string or another.
    """
    name = full_name(first_name, last_name)
    place = where_i_am_from(hometown)
    if place == True:
        print "Hi, " + name + ", we're from the same place!"
    else:
        print "Hi, " + name + ", where are you from?"

# test code for input: name_and_origin_greeting("Reno", "Christina", "Westbrook")

###############################################################################

# PART TWO

# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry."


def is_berry(fruit):
    """Determines if fruit is a berry"""
    if str(fruit) == "strawberry":
        return True
    elif str(fruit) == "cherry":
        return True
    elif str(fruit) == "blackberry":
        return True
    else:
        return False

# (b) Write another function, shipping_cost(), which calculates shipping cost
#     by taking a fruit name as a string and calling the is_berry() function
#     within the shipping_cost() function. Your function should return 0 if
#     is_berry() == True, and 5 if is_berry() == False.


def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    if is_berry(fruit) == True:
        return 0
    elif is_berry(fruit) == False:
        return 5


# 2. Make a function that takes in a number and a list of numbers. It should
#    return a new list containing the elements of the input list, along with
#    given number, which should be at the end of the new list.


def append_to_list(lst, num):
    """Creates a new list consisting of the old list with the given number
       added to the end."""
    new_list = lst + [num]
    return new_list




# 3. Write a function calculate_price to calculate an item's total cost by
#    adding tax, and any fees required by state law.

#    Your function will take as parameters (in this order): the base price of
#    the item, a two-letter state abbreviation, and the tax percentage (as a
#    two-digit decimal, so, for instance, 5% will be .05). If the user does not
#    provide a tax rate it should default to 5%.

#    CA law requires stores to collect a 3% recycling fee, PA requires a $2
#    highway safety fee, and in MA, there is a commonwealth fund fee of $1 for
#    items with a base price under $100 and $3 for items $100 or more. Fees are
#    added *after* the tax is calculated.

#    Your function should return the total cost of the item, including tax and
#    fees.


# I was stuck on this for a while but if I had more time I'd minimize the repeating
# factors.
def calculate_price(base_price, state_abbreviation, tax_percentage=.05):
    """This list takes in three parameters and adds fees and taxes onto 
    certain states that have specific fees added on
    """
    tax = int(base_price) * float(tax_percentage)
    base_plus_tax = int(base_price) + float(tax)
    if str(state_abbreviation) == "CA":
        total_cost = base_plus_tax + (base_plus_tax * float(.03))
        total_cost_one_decimal = format(total_cost, '.1f')
        return float(total_cost_one_decimal)
    elif str(state_abbreviation) == "PA":
        total_cost = base_plus_tax + 2
        total_cost_one_decimal = format(total_cost, '.1f')
        return float(total_cost_one_decimal)
    elif str(state_abbreviation) == "MA":
        if int(base_price) < 100:
            total_cost = base_plus_tax + 1
            total_cost_one_decimal = format(total_cost, '.1f')
            return float(total_cost_one_decimal)
        elif int(base_price) > 100:
            total_cost = base_plus_tax + 3
            total_cost_one_decimal = format(total_cost, '.1f')
            return float(total_cost_one_decimal)
    # I can't get this test failure to resolve without adding an elif for "OR, 
    # since every other test seems to require one decimal place but this one doesn't
    elif str(state_abbreviation) == "OR":
        total_cost = int(base_plus_tax)
        total_cost_one_decimal = format(total_cost, '.0f')
        return int(total_cost_one_decimal)
    else:
        total_cost = int(base_plus_tax)
        total_cost_one_decimal = format(total_cost, '.1f')
        return float(total_cost_one_decimal)




###############################################################################

# PART THREE: ADVANCED

# NOTE: We haven't given you function signatures and docstrings for these, so
# you'll need to write your own. These functions also aren't included in the
# doctests above, so make sure to test them on your own.


# 1. Make a new function that takes in a list and any number of additional
# arguments, appends them to the list, and returns the entire list. Hint: this
# isn't something we've discussed yet in class; you might need to google how to
# write a Python function that takes in an arbitrary number of arguments.


def list_with_additional_arguments(a_list, *arguments):
    """ Trying out making a function with a list as one argument and an unknown 
    number of arguments for the second argument
    """
    # not working, hope this lecture is soon!
    return a_list.append(arguments)

# attempting with this code: list_with_additional_arguments(a_list["listtt", "of", "stuff"], "randomz")


# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner
# function.

def taking_a_word(a_word):
    """taking a word input in a function, in a nested function mulptilying the 
    word input by three, then inputing a word into the original function and 
    outputting via the main function, which should output the argument times 3
    plus the word said once
    """
    def multiplying_word(a_word):
        return a_word * 3
    inner_output = multiplying_word(a_word)
    print a_word + ", " + inner_output


# taking_a_word("Whaaat")

# Example:

#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


###############################################################################

# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
