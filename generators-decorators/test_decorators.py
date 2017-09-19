import decorators

import unittest

class Evaluate(unittest.TestCase):

    def test_double_result(self):
        @decorators.double_result
        def add(a,b):
            return a+b

        self.assertEqual(add(2,2), 8)

    def test_only_ints(self):
        @decorators.only_ints
        def add(a,b):
            return a+b

        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(2,"2"), "Please only invoke with integers")

    def test_only_even_parameters(self):
        @decorators.only_even_parameters
        def add(a,b):
            return a+b

        self.assertEqual(add(2,2), 4)
        self.assertEqual(add(2,11), "Please add even numbers")

    def test_authorize_user(self):
        @decorators.authorize_user
        def admin_add(*args, **kwargs):
            return args[0]+args[1]

        self.assertEqual(admin_add(2,2), "Not Authorized")
        self.assertEqual(admin_add(2,2, admin=True), 4)

if __name__ == '__main__':
    unittest.main()
