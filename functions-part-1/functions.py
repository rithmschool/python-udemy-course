def product(a, b):
    return a * b


def return_day(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num - 1]
    except IndexError as e:
        return None


def last_element(l):
    try:
        return l[-1]
    except IndexError as e:
        return None


def number_compare(a, b):
    if a > b:
        return "First is greater"
    elif b > a:
        return "Second is greater"
    return "Numbers are equal"


def single_letter_count(string, letter):
    return string.lower().count(letter.lower())


def multiple_letter_count(string):
    return {letter: string.count(letter) for letter in string}


def list_manipulation(collection, command, location, value=None):
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
    return string == string[::-1]


def frequency(collection, searchTerm):
    return collection.count(searchTerm)


def flip_case(string, letter):
    return "".join([char.swapcase() if char.lower() == letter.lower() else char for char in string])


def multiply_even_numbers(lst):
    total = 1
    for val in lst:
        if val % 2 == 0:
            total = total * val
    return total


def capitalize(string):
    return string[:1].upper() + string[1:]


def compact(l):
    return [val for val in l if val]


def intersection(l1, l2):
    return [val for val in l1 if val in l2]


def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


def mode(collection):
    count = {val: collection.count(val) for val in collection}
    # find the highest value (the most frequent number)
    max_value = max(count.values())
    # now we need to see at which index the highest value is at
    correct_index = list(count.values()).index(max_value)
    # finally, return the correct key for the correct index (we have to convert cou)
    return list(count.keys())[correct_index]
