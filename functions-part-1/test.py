import functions

import unittest

class Evaluate(unittest.TestCase):
    def test_product(self):
        """ It should return one number multiplied by another """
        self.assertEqual(functions.product(2,2),4)
        self.assertEqual(functions.product(2,-2),-4)

    def test_return_day(self):
        """ It should return the day of the week or None"""
        self.assertEqual(functions.return_day(1),"Sunday")
        self.assertEqual(functions.return_day(2),"Monday")
        self.assertEqual(functions.return_day(3),"Tuesday")
        self.assertEqual(functions.return_day(4),"Wednesday")
        self.assertEqual(functions.return_day(5),"Thursday")
        self.assertEqual(functions.return_day(6),"Friday")
        self.assertEqual(functions.return_day(41),None)


    def test_last_element(self):
        """ It should return the last element in a list """
        self.assertEqual(functions.last_element([1,2,3]),3)
        self.assertEqual(functions.last_element([]),None)


    def test_number_compare(self):
        """ It should compare two numbers and return which one is greater """
        self.assertEqual(functions.number_compare(1,1),"Numbers are equal")
        self.assertEqual(functions.number_compare(1,0),"First is greater")
        self.assertEqual(functions.number_compare(2,4),"Second is greater")

    def test_single_letter_count(self):
        """ It should return one number minus another """
        self.assertEqual(functions.single_letter_count("Hello World", "h"), 1)
        self.assertEqual(functions.single_letter_count("Hello World", "z"), 0)
        self.assertEqual(functions.single_letter_count("HelLo World", "l"), 3)

    def test_multiple_letter_count(self):
        """ It should return a dict with each letter and number of times it appears """
        self.assertEqual(functions.multiple_letter_count("awesome"), {'a': 1, 'e': 2, 'm': 1, 'o': 1, 's': 1, 'w': 1})

    def test_list_manipulation(self):
        self.assertEqual(functions.list_manipulation([1,2,3], "remove", "end"),3)
        self.assertEqual(functions.list_manipulation([1,2,3], "remove", "beginning"), 1)
        self.assertEqual(functions.list_manipulation([1,2,3], "add", "beginning", 20), [20,1,2,3])
        self.assertEqual(functions.list_manipulation([1,2,3], "add", "end", 30), [1,2,3,30])

    def test_palindrome(self):
        self.assertEqual(functions.is_palindrome('testing'),False)
        self.assertEqual(functions.is_palindrome('tacocat'),True)
        self.assertEqual(functions.is_palindrome('hannah'),True)
        self.assertEqual(functions.is_palindrome('robert'),False)
        self.assertEqual(functions.is_palindrome('amanaplanacanalpanama'),True)

    def test_frequency(self):
        """ It should return the count of a value """
        self.assertEqual(functions.frequency([1,2,3,4,4,4], 4), 3)
        self.assertEqual(functions.frequency([True, False, True, True], False), 1)

    def test_flip_case(self):
        self.assertEqual(functions.flip_case("Hardy har har", "h"), "hardy Har Har")

    def test_multiply_even_numbers(self):
        self.assertEqual(functions.multiply_even_numbers([2,3,4,5,6]), 48)

    def test_capitalize(self):
        self.assertEqual(functions.capitalize("tim"), "Tim")
        self.assertEqual(functions.capitalize("matt"), "Matt")

    def test_compact(self):
        self.assertEqual(functions.compact([0,1,2,"",[], False, {}, None, "All done"]), [1,2, "All done"])

    def test_intersection(self):
        self.assertEqual(functions.intersection([1,2,3], [2,3,4]), [2,3])

    def test_partition(self):
        def isEven(num):
            return num % 2 == 0

        self.assertEqual(functions.partition([1,2,3,4], isEven), [[2,4],[1,3]])

    def test_mode(self):
        self.assertEqual(functions.mode([2,4,1,2,3,3,4,4,5,4,4,6,4,6,7,4]), 4)

if __name__ == '__main__':
    unittest.main()
