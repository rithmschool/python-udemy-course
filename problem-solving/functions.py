def reverse_string(string):
    s = ''
    i = len(string) - 1
    while(i >= 0):
        s += string[i]
        i -= 1
    return s


def list_check(vals):
    return all(type(l) == list for l in vals)


def remove_every_other(lst):
    return [val for i, val in enumerate(lst) if i % 2 == 0]


def sum_pairs(ints, s):
    already_visited = set()
    for i in ints:
        difference = s - i
        if difference in already_visited:
            return [difference, i]
        already_visited.add(i)
    return []


def vowel_count(string):
    lower_s = string.lower()
    return {letter: lower_s.count(letter) for letter in string if letter in "aeiou"}


def titleize(string):
    return ' '.join(s[0].upper() + s[1:] for s in string.split(' '))


def find_factors(num):
    factors = []
    i = 1
    while(i <= num):
        if num % i == 0:
            factors.append(i)
        i += 1
    return factors


def includes(item, val, start=None):
    if type(item) == dict:
        return val in item.values()
    if start is None:
        return val in item
    return val in item[start:]


def repeat(string, num):
    if(num == 0):
        return ''
    i = 0
    newStr = ''
    while(i < num):
        newStr += string
        i += 1
    return newStr


def truncate(string, n):
    if n < 3:
        return "Truncation must be at least 3 characters."
    if n > len(string) + 2:
        return string

    return string[:n - 3] + "..."


def two_list_dictionary(keys, values):
    collection = {}

    for idx, val in enumerate(keys):
        if idx < len(values):
            collection[keys[idx]] = values[idx]
        else:
            collection[keys[idx]] = None

    return collection


def range_in_list(lst, start=0, end=None):
    if end is None:
      end = len(lst)
    return sum(lst[start:end + 1])


def same_frequency(num1, num2):
    d1 = {letter: str(num1).count(letter) for letter in str(num1)}
    d2 = {letter: str(num2).count(letter) for letter in str(num2)}

    for key, val in d1.items():
        if not key in d2.keys():
            return False
        elif d2[key] != d1[key]:
            return False
    return True


def nth(lst, idx):
    if idx >= 0:
        return lst[idx]
    return lst[idx + len(lst)]


def find_the_duplicate(lst):
    counter = {}
    for val in lst:
        if val in counter:
            counter[val] += 1
        else:
            counter[val] = 1
    for key in counter.keys():
        if counter[key] > 1:
            return int(key)


def sum_up_diagonals(lst):
    total = 0

    for i, val in enumerate(lst):
        total += lst[i][i]
        total += lst[i][-1 - i]
    return total


def find_twins(lst):
    freq = {val: lst.count(val) for val in lst}
    for key in freq.keys():
        if freq[key] > 1:
            return key


def min_max_key_in_dictionary(d):
    keys = d.keys()
    return [min(keys), max(keys)]


def find_greater_numbers(lst):
    count = 0
    i = 0
    j = 1
    while i < len(lst):
        while j < len(lst):
            if lst[j] > lst[i]:
                count += 1
            j += 1
        j = i + 1
        i += 1
    return count


def two_oldest_ages(ages):
    return sorted(ages)[-2:]


def is_odd_string(string):
    total = sum((ord(c) - 96) for c in string.lower()) or 0
    return total % 2 == 1


def valid_parentheses(parens):
    count = 0
    i = 0
    while i < len(parens):
        if parens[i] == '(':
            count += 1
        if parens[i] == ')':
            count -= 1
        if count < 0:
            return False
        i += 1
    return count == 0


def three_odd_numbers(lst):
    i = 0
    while(i < (len(lst) - 2)):
        total = 0
        j = i
        while(j <= i + 2):
            total += lst[j]
            j += 1

        if (j - i) % 3 == 0 and total % 2 != 0:
            return True

        i += 1
    return False


def reverse_vowels(s):
    vowels = "aeiou"
    string = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if string[i].lower() not in vowels:
            i += 1
        elif string[j].lower() not in vowels:
            j -= 1
        else:
            string[i], string[j] = string[j], string[i]
            i += 1
            j -= 1
    return "".join(string)
