from decorators import *
import unittest
from unittest.mock import patch, call

class Evaluate(unittest.TestCase):

    @patch('builtins.print')
    def test_show_args(self, mock):
        @show_args
        def do_nothing(*args, **kwargs):
            pass

        do_nothing(1, 2, 3,a="hi",b="bye")
        self.assertTrue(all(c in [
            call('Here are the args:', (1, 2, 3)),
            call('Here are the kwargs:', {"a": "hi", "b": "bye"}),
            call('Here are the args: (1, 2, 3)'),
            call('Here are the kwargs: {"a": "hi", "b": "bye"}'),
            call('Here are the args: (1, 2, 3)\nHere are the kwargs: {"a": "hi", "b": "bye"}'),
            call('Here are the args: (1, 2, 3) \nHere are the kwargs: {"a": "hi", "b": "bye"}')
        ] for c in mock.call_args_list))

    def test_ensure_fewer_than_three_args(self):
        @ensure_fewer_than_three_args
        def add_all(*nums):
            return sum(nums)

        self.assertEqual(add_all(),0)
        self.assertEqual(add_all(1),1)
        self.assertEqual(add_all(1,2),3)
        self.assertEqual(add_all(1,2,3),"Too many arguments!")
        self.assertEqual(add_all(1,2,3,4,5,6),"Too many arguments!")

    def test_only_ints(self):
        @only_ints 
        def add(x, y):
            return x + y

        self.assertEqual(add(1,2),3)
        self.assertEqual(add("1","2"), "Please only invoke with integers.")

    def test_ensure_authorized(self):
        @ensure_authorized
        def show_secrets(*args, **kwargs):
            return "Shh! Don't tell anybody!"

        self.assertEqual(show_secrets(role="admin"), "Shh! Don't tell anybody!")
        self.assertEqual(show_secrets(role="nobody"), "Unauthorized")
        self.assertEqual(show_secrets(a="b"), "Unauthorized")

    @patch('builtins.print')
    @patch('decorators.sleep')
    def test_delay(self, print_mock, sleep_mock):
        @delay(3)
        def say_hi():
            return "hi"

        say_hi()
        sleep_mock.assert_called_with("Waiting 3s before running say_hi")
        print_mock.assert_called_with(3)

if __name__ == '__main__':
    unittest.main()
