import generators

import unittest


class Evaluate(unittest.TestCase):

    def test_accumulate(self):
        gen = generators.accumulate(10)
        self.assertEqual(next(gen), 1)
        self.assertEqual(next(gen), 3)
        self.assertEqual(next(gen), 6)
        self.assertEqual(next(gen), 10)
        self.assertEqual(next(gen), 15)
        self.assertEqual(next(gen), 21)

        sol = [val for val in generators.accumulate(40)]
        self.assertEqual(sol, [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210,
                               231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 561, 595, 630, 666, 703, 741, 780, 820])

    def test_fib(self):
        gen = generators.fib(10)
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

        l = [val for val in generators.fib(15)]
        sol = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

        self.assertEqual(l, sol)


if __name__ == '__main__':
    unittest.main()
