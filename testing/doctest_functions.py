def product(a, b):
    """
    >>> product(2, 2)
    4

    >>> product(2, -2)
    -4
    """
    return a * b


def return_day(num):
    """
    >>> return_day(1)
    'Sunday'

    >>> return_day(2)
    'Monday'

    >>> return_day(3)
    'Tuesday'

    >>> return_day(4)
    'Wednesday'

    >>> return_day(5)
    'Thursday'

    >>> return_day(6)
    'Friday'

    >>> return_day(7)
    'Saturday'
    
    >>> return_day(41)
    """
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num - 1]
    except IndexError as e:
        return None


def last_element(l):
    """
    >>> last_element([1, 2, 3])
    3

    >>> last_element([])
    """
    try:
        return l[-1]
    except IndexError as e:
        return None


def number_compare(a, b):
    """
    >>> number_compare(1, 1)
    'Numbers are equal'

    >>> number_compare(1, 0)
    'First is greater'

    >>> number_compare(2, 4)
    'Second is greater'
    """
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"


def single_letter_count(string, letter):
    """
    >>> single_letter_count("Hello World", "h")
    1

    >>> single_letter_count("Hello World", "z")
    0

    >>> single_letter_count("HelLo World", "l")
    3
    """
    return string.lower().count(letter.lower())


def multiple_letter_count(string):
    """
    >>> multiple_letter_count("awesome")
    {'a': 1, 'w': 1, 'e': 2, 's': 1, 'o': 1, 'm': 1}
    """
    return {letter: string.count(letter) for letter in string}


def list_manipulation(collection, command, location, value=None):
    """
    >>> list_manipulation([1, 2, 3], "remove", "end")
    3

    >>> list_manipulation([1, 2, 3], "remove", "beginning")
    1

    >>> list_manipulation([1, 2, 3], "add", "beginning", 20)
    [20, 1, 2, 3]

    >>> list_manipulation([1, 2, 3], "add", "end", 30)
    [1, 2, 3, 30]
    """
    if(command == "remove" and location == "end"):
        return collection.pop()
    elif(command == "remove" and location == "beginning"):
        return collection.pop(0)
    elif(command == "add" and location == "beginning"):
        collection.insert(0, value)
        return collection
    elif(command == "add" and location == "end"):
        collection.append(value)
        return collection


def is_palindrome(string):
    """
    >>> is_palindrome('testing')
    False

    >>> is_palindrome('tacocat')
    True

    >>> is_palindrome('hannah')
    True

    >>> is_palindrome('robert')
    False

    >>> is_palindrome('amanaplanacanalpanama')
    True
    """
    return string == string[::-1]


def frequency(collection, searchTerm):
    """
    >>> frequency([1, 2, 3, 4, 4, 4], 4)
    3

    >>> frequency([True, False, True, True], False)
    1
    """
    return collection.count(searchTerm)


def flip_case(string, letter):
    """
    >>> flip_case("Hardy har har", "h")
    'hardy Har Har'
    """
    return "".join([char.swapcase() if char.lower() == letter.lower() else char for char in string])


def multiply_even_numbers(lst):
    """
    >>> multiply_even_numbers([2, 3, 4, 5, 6])
    48
    """
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total


def capitalize(string):
    """
    >>> capitalize("colt")
    'Colt'

    >>> capitalize("matt")
    'Matt'
    """
    return string[:1].upper() + string[1:]


def compact(l):
    """
    >>> compact([0, 1, 2, "", [], False, {}, None, "All done"])
    [1, 2, 'All done']
    """
    return [val for val in l if val]


def intersection(l1, l2):
    """
    >>> intersection([1, 2, 3], [2, 3, 4])
    [2, 3]
    """
    return [val for val in l1 if val in l2]


def partition(lst, fn):
    """
    >>> def isEven(num):
    ...     return num % 2 == 0
    >>> partition([1, 2, 3, 4], isEven)
    [[2, 4], [1, 3]]
    """
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


def mode(collection):
    """
    >>> mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4])
    4
    """
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]
