from solutions import *
import unittest
from unittest.mock import patch, call

class Evaluate(unittest.TestCase):

    def test_week(self):
        days = week()
        self.assertEqual(next(days), 'Monday')
        self.assertEqual(next(days), 'Tuesday')
        self.assertEqual(next(days), 'Wednesday')
        self.assertEqual(next(days), 'Thursday')
        self.assertEqual(next(days), 'Friday')
        self.assertEqual(next(days), 'Saturday')
        self.assertEqual(next(days), 'Sunday')
        with self.assertRaises(StopIteration):
            next(days)

    def test_make_song(self):
        kombucha_song = make_song(5, "kombucha")
        self.assertEqual(
            next(kombucha_song),
            '5 bottles of kombucha on the wall.'
        )
        self.assertEqual(
            next(kombucha_song),
            '4 bottles of kombucha on the wall.'
        )
        self.assertEqual(
            next(kombucha_song),
            '3 bottles of kombucha on the wall.'
        )
        self.assertEqual(
            next(kombucha_song),
            '2 bottles of kombucha on the wall.'
        )
        self.assertEqual(
            next(kombucha_song),
            'Only 1 bottle of kombucha left!'
        )
        self.assertEqual(
            next(kombucha_song),
            'No more kombucha!'
        )
        with self.assertRaises(StopIteration):
            next(kombucha_song)

    def test_make_song_default_arguments(self):
        default_song = make_song()
        self.assertEqual(
            next(default_song),
            '99 bottles of soda on the wall.'
        )

    def test_get_multiples(self):
        evens = get_multiples(2, 3)
        self.assertEqual(next(evens), 2)
        self.assertEqual(next(evens), 4)
        self.assertEqual(next(evens), 6)
        with self.assertRaises(StopIteration):
            next(evens)

    def test_get_multiples_default_arguments(self):
        default_multiples = get_multiples()
        self.assertEqual(
            list(default_multiples),
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        )

    def test_get_unlimited_multiples(self):
        sevens = get_unlimited_multiples(7)
        ones = get_unlimited_multiples()
        self.assertEqual(
            [next(sevens) for i in range(15)],
            [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]
        )
        self.assertEqual(
            [next(ones) for i in range(20)],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
        )

    def test_next_prime(self):
        primes = next_prime()
        self.assertEqual(
            [next(primes) for i in range(25)],
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
                43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        )

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
    @patch('solutions.sleep')
    def test_delay(self, print_mock, sleep_mock):
        @delay(3)
        def say_hi():
            return "hi"

        say_hi()
        sleep_mock.assert_called_with("Waiting 3s before running say_hi")
        print_mock.assert_called_with(3)

if __name__ == '__main__':
    unittest.main()
