import solutions

import unittest


class Evaluate(unittest.TestCase):

    def test_accumulate(self):
        gen = solutions.accumulate(10)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 6)
        self.assertEqual(next(gen), 10)
        self.assertEqual(next(gen), 15)
        self.assertEqual(next(gen), 21)

        sol = [val for val in solutions.accumulate(40)]
        self.assertEqual(sol, [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210,
                               231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820])

    def test_fib(self):
        gen = solutions.fib(10)
        self.assertEqual(next(gen), 0)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 2)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 5)
        self.assertEqual(next(gen), 8)
        self.assertEqual(next(gen), 13)
        self.assertEqual(next(gen), 21)
        self.assertEqual(next(gen), 34)

        l = [val for val in solutions.fib(15)]
        sol = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

        self.assertEqual(l, sol)

    def test_double_result(self):
        @solutions.double_result
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 2), 8)

    def test_only_ints(self):
        @solutions.only_ints
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(2, "2"), "Please only invoke with integers")

    def test_only_even_parameters(self):
        @solutions.only_even_parameters
        def add(a, b):
            return a + b

        self.assertEqual(add(2, 2), 4)
        self.assertEqual(add(2, 11), "Please add even numbers")

    def test_authorize_user(self):
        @solutions.authorize_user
        def admin_add(*args, **kwargs):
            return args[0] + args[1]

        self.assertEqual(admin_add(2, 2), "Not Authorized")
        self.assertEqual(admin_add(2, 2, admin=True), 4)


if __name__ == '__main__':
    unittest.main()
