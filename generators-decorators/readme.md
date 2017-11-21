# Decorators Exercise

Try to implement the following functions.

#### `show_args`

Write a function called `show_args` which accepts a function and returns another function. Before invoking the function passed to it, `show_args` should be responsible for printing two things: a tuple of the positional arguments, and a dictionary of the keyword arguments.

#### `ensure_fewer_than_three_args`

Write a function called `ensure_fewer_than_three_args` which accepts a function and returns another function. The function passed to it should only be invoked if there are fewer than three positional arguments passed to it. Otherwise, the inner function should return "Too many arguments!"

#### `only_ints`

Write a function called `only_ints` which accepts a function and returns another function. The function passed to it should only be invoked if all of the arguments passed to it are integers. Otherwise the inner function should return "Please only invoke with integers".

#### `ensure_authorized`

Write a function called `ensure_authorized` which accepts a function and returns another function. The function passed to it should only be invoked if there exists a keyword argument with a name of "role" and a value of "admin". Otherwise, the inner function should return "Unauthorized"

#### `delay`

Write a function called `delay` which accepts a time and returns an inner function that accepts a function. When used as a decorator, `delay` will wait to execute the function being decorated by the amount of time passed into it. Before starting the timer, `delay` will also print a message informing the user that there will be a delay before the decorated function gets run.

(Hint: take a look at the sleep function from the built-in time module if you want to pause code execution for a certain amount of time.)

To get more details about the expected outputs for these decorators, try to read through the tests!
