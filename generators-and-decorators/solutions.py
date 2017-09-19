from functools import wraps

# Generators Exercise
def accumulate(end):
    total = 0
    for num in range(1, end+1):
        total += num
        yield total

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Decorators Exercises
def double_result(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        return fn(*args, **kwargs) * 2
    return inner

def only_ints(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers"
        return fn(*args, **kwargs)
    return inner

def only_even_parameters(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if arg % 2 != 0]):
            return "Please add even numbers"
        return fn(*args, **kwargs)
    return inner

def authorize_user(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if kwargs.get('admin') or 'secret' in args:
            return fn(*args, **kwargs)
        return 'Not Authorized'
    return inner

