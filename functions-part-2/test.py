import functions

import unittest


class Evaluate(unittest.TestCase):
    def test_calculate(self):
        self.assertEqual(functions.calculate(make_float=False, operation='add',
                                             message='You just added', first=2, second=4), "You just added 6")
        self.assertEqual(functions.calculate(
            make_float=True, operation='divide', first=3.5, second=5), "The result is 0.7")

    def test_sum_even_values(self):
        self.assertEqual(functions.sum_even_values(1, 2, 3, 4, 5, 6), 12)
        self.assertEqual(functions.sum_even_values(4, 2, 1, 10), 16)
        self.assertEqual(functions.sum_even_values(1), 0)

    def test_triple_and_filter(self):
        self.assertEqual(functions.triple_and_filter([1, 2, 3, 4]), [12])
        self.assertEqual(functions.triple_and_filter([6, 8, 10, 12]), [24, 36])

    def test_extract_full_name(self):
        names = [{'first': 'Elie', 'last': 'Schoppik'},
                 {'first': 'Colt', 'last': 'Steele'}]
        self.assertEqual(functions.extract_full_name(
            names), ['Elie Schoppik', 'Colt Steele'])

    def test_sum_floats(self):
        self.assertEqual(functions.sum_floats(1.5, 2.4, 'awesome', [], 1), 3.9)

    def test_running_average(self):
        rAvg = functions.running_average()
        self.assertEqual(rAvg(10), 10.0)
        self.assertEqual(rAvg(11), 10.5)
        self.assertEqual(rAvg(12), 11)

        rAvg2 = functions.running_average()
        self.assertEqual(rAvg2(1), 1)
        self.assertEqual(rAvg2(3), 2)

    def test_letter_counter(self):
        counter = functions.letter_counter('Amazing')
        self.assertEqual(counter('a'), 2)
        self.assertEqual(counter('m'), 1)

        counter2 = functions.letter_counter('This Is Really Fun!')
        self.assertEqual(counter2('i'), 2)
        self.assertEqual(counter2('t'), 1)

    def test_once(self):
        def add(a, b):
            return a + b

        oneAddition = functions.once(add)

        self.assertEqual(oneAddition(2, 2), 4)
        self.assertEqual(oneAddition(2, 2), None)
        self.assertEqual(oneAddition(12, 200), None)


if __name__ == '__main__':
    unittest.main()
