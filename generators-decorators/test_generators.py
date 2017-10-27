from generators import *
import unittest

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

if __name__ == '__main__':
    unittest.main()
