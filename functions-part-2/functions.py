def calculate(**kwargs):
    first = kwargs.get('first', 0)
    second = kwargs.get('second', 0)
    operation_lookup = {
        'add': first + second,
        'subtract': first - second,
        'divide': first / second,
        'multiply': first / second
    }
    is_float = kwargs.get('make_float', False)
    operation_value = operation_lookup[kwargs.get('operation', '')]
    if is_float:
        final = "{} {}".format(kwargs.get('message','The result is'), float(operation_value))
    else:
        final = "{} {}".format(kwargs.get('message','The result is'), int(operation_value))
    return final

def sum_even_values(*args):
    return sum(arg for arg in args if arg % 2 == 0) or 0

def triple_and_filter(lst):
    return list(filter(lambda x: x % 4 == 0, map(lambda x: x*3, lst)))

def extract_full_name(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))

def sum_floats(*args):
    return sum(arg for arg in args if type(arg) == float) or 0

def running_average():
    running_average.accumulator = 0
    running_average.size = 0

    def inner(number):
        running_average.accumulator += number
        running_average.size += 1
        return running_average.accumulator / running_average.size

    return inner

def letter_counter(s):
    letter_counter.val = s
    def inner(char):
        return len(list(c.lower() for c in letter_counter.val.lower() if c == char))
    return inner

def once(fn):
    fn.is_called = False
    def inner(*args):
        if not(fn.is_called):
            fn.is_called = True
            return fn(*args)
    return inner
