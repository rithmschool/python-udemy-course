import functions

import unittest


class Evaluate(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(functions.reverse_string('awesome'), 'emosewa')
        self.assertEqual(functions.reverse_string('Colt'), 'tloC')
        self.assertEqual(functions.reverse_string('Elie'), 'eilE')

    def test_list_check(self):
        self.assertEqual(functions.list_check(
            [[], [1], [2, 3], (1, 2)]), False)
        self.assertEqual(functions.list_check(
            [1, True, [], [1], [2, 3]]), False)
        self.assertEqual(functions.list_check([[], [1], [2, 3]]), True)

    def test_remove_every_other(self):
        self.assertEqual(functions.remove_every_other(
            [1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(functions.remove_every_other(
            [5, 1, 2, 4, 1]), [5, 2, 1])
        self.assertEqual(functions.remove_every_other([1]), [1])

    def test_sum_pairs(self):
        self.assertEqual(functions.sum_pairs([4, 2, 10, 5, 1], 6), [4, 2])
        self.assertEqual(functions.sum_pairs([11, 20, 4, 2, 1, 5], 100), [])

    def test_vowel_count(self):
        self.assertEqual(functions.vowel_count(
            'awesome'), {'a': 1, 'e': 2, 'o': 1})
        self.assertEqual(functions.vowel_count('Elie'), {'e': 2, 'i': 1})
        self.assertEqual(functions.vowel_count('Colt'), {'o': 1})

    def test_titleize(self):
        self.assertEqual(functions.titleize(
            'this is awesome'), "This Is Awesome")
        self.assertEqual(functions.titleize(
            'oNLy cAPITALIZe fIRSt'), "ONLy CAPITALIZe FIRSt")

    def test_find_factors(self):
        self.assertEqual(functions.find_factors(10), [1, 2, 5, 10])
        self.assertEqual(functions.find_factors(11), [1, 11])
        self.assertEqual(functions.find_factors(111), [1, 3, 37, 111])
        self.assertEqual(functions.find_factors(
            321421), [1, 293, 1097, 321421])
        self.assertEqual(functions.find_factors(412146), [
                         1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126, 3271, 6542, 9813, 19626, 22897, 29439, 45794, 58878, 68691, 137382, 206073, 412146])

    def test_includes(self):
        self.assertEqual(functions.includes([1, 2, 3], 1), True)
        self.assertEqual(functions.includes([1, 2, 3], 1, 2), False)
        self.assertEqual(functions.includes({'a': 1, 'b': 2}, 1), True)
        self.assertEqual(functions.includes({'a': 1, 'b': 2}, 'a'), False)
        self.assertEqual(functions.includes('abcd', 'b'), True)
        self.assertEqual(functions.includes('abcd', 'e'), False)

    def test_repeat(self):
        self.assertEqual(functions.repeat('*', 3), '***')
        self.assertEqual(functions.repeat('abc', 2), 'abcabc')
        self.assertEqual(functions.repeat('abc', 0), '')

    def test_truncate(self):
        self.assertEqual(functions.truncate("Super cool", 2),
                         "Truncation must be at least 3 characters.")
        self.assertEqual(functions.truncate("Super cool", 1),
                         "Truncation must be at least 3 characters.")
        self.assertEqual(functions.truncate("Super cool", 0),
                         "Truncation must be at least 3 characters.")
        self.assertEqual(functions.truncate("Hello World", 6), "Hel...")
        self.assertEqual(functions.truncate(
            "Problem solving is the best!", 10), "Problem...")
        self.assertEqual(functions.truncate(
            "Another test", 12), "Another t...")
        self.assertEqual(functions.truncate("Woah", 4), "W...")
        self.assertEqual(functions.truncate("Woah", 3), "...")
        self.assertEqual(functions.truncate("Yo", 100), "Yo")
        self.assertEqual(functions.truncate(
            "Holy guacamole!", 152), "Holy guacamole!")

    def test_two_list_dictionary(self):
        self.assertEqual(functions.two_list_dictionary(['a', 'b', 'c', 'd'], [
                         1, 2, 3]), {'a': 1, 'b': 2, 'c': 3, 'd': None})
        self.assertEqual(functions.two_list_dictionary(
            ['a', 'b', 'c'], [1, 2, 3, 4]), {'a': 1, 'b': 2, 'c': 3})
        self.assertEqual(functions.two_list_dictionary(
            ['x', 'y', 'z'], [1, 2]), {'x': 1, 'y': 2, 'z': None})

    def test_range_in_list(self):
        self.assertEqual(functions.range_in_list([1, 2, 3, 4], 0, 2), 6)
        self.assertEqual(functions.range_in_list([1, 2, 3, 4], 0, 3), 10)
        self.assertEqual(functions.range_in_list([1, 2, 3, 4], 1), 9)
        self.assertEqual(functions.range_in_list([1, 2, 3, 4]), 10)
        self.assertEqual(functions.range_in_list([1, 2, 3, 4], 0, 100), 10)
        self.assertEqual(functions.range_in_list([], 0, 1), 0)

    def test_same_frequency(self):
        self.assertEqual(functions.same_frequency(551122, 221515), True)
        self.assertEqual(functions.same_frequency(321142, 3212215), False)
        self.assertEqual(functions.same_frequency(1212, 2211), True)

    def test_nth(self):
        array = ['a', 'b', 'c', 'd']
        self.assertEqual(functions.nth(array, 1), 'b')
        self.assertEqual(functions.nth(array, -2), 'c')
        self.assertEqual(functions.nth(array, 0), 'a')
        self.assertEqual(functions.nth(array, -4), 'a')
        self.assertEqual(functions.nth(array, -1), 'd')
        self.assertEqual(functions.nth(array, 3), 'd')

    def test_find_the_duplicate(self):
        self.assertEqual(functions.find_the_duplicate([1, 2, 1, 4, 3, 12]), 1)
        self.assertEqual(functions.find_the_duplicate(
            [6, 1, 9, 5, 3, 4, 9]), 9)
        self.assertEqual(functions.find_the_duplicate([2, 1, 3, 4]), None)

    def test_sum_diagonals(self):
        list1 = [
            [1, 2],
            [3, 4]
        ]

        self.assertEqual(functions.sum_up_diagonals(list1), 10)

        list2 = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

        self.assertEqual(functions.sum_up_diagonals(list2), 30)

        list3 = [
            [4, 1, 0],
            [-1, -1, 0],
            [0, 0, 9]
        ]

        self.assertEqual(functions.sum_up_diagonals(list3), 11)

        list4 = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16]
        ]

        self.assertEqual(functions.sum_up_diagonals(list4), 68)

    def test_find_twins(self):
        self.assertEqual(functions.find_twins([4, 1, 6, 1, 5]), 1)
        self.assertEqual(functions.find_twins([2, 3, 6, 34, 7, 8, 2]), 2)
        self.assertEqual(functions.find_twins([3, 6, 9, 2, 4, 3, 1, 0]), 3)
        self.assertEqual(functions.find_twins([]), None)
        self.assertEqual(functions.find_twins([3, 1, 4, 2, 5]), None)

    def test_min_max_key_in_dictionary(self):
        self.assertEqual(functions.min_max_key_in_dictionary(
            {2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}), [1, 10])
        self.assertEqual(functions.min_max_key_in_dictionary(
            {1: "Elie", 4: "Matt", 3: "Tim"}), [1, 4])

    def test_find_greater_numbers(self):
        self.assertEqual(functions.find_greater_numbers([1, 2, 3]), 3)
        self.assertEqual(functions.find_greater_numbers([6, 1, 2, 7]), 4)
        self.assertEqual(functions.find_greater_numbers([5, 4, 3, 2, 1]), 0)
        self.assertEqual(functions.find_greater_numbers([]), 0)

    def test_two_oldest_ages(self):
        self.assertEqual(functions.two_oldest_ages([1, 2, 10, 8]), [8, 10])
        self.assertEqual(functions.two_oldest_ages([6, 1, 9, 10, 4]), [9, 10])
        self.assertEqual(functions.two_oldest_ages(
            [4, 25, 3, 20, 19, 5]), [20, 25])

    def test_is_odd_string(self):
        self.assertEqual(functions.is_odd_string('a'), True)
        self.assertEqual(functions.is_odd_string('aaaa'), False)
        self.assertEqual(functions.is_odd_string('amazing'), True)
        self.assertEqual(functions.is_odd_string('veryfun'), True)
        self.assertEqual(functions.is_odd_string('veryfunny'), False)

    def test_valid_parenthesis(self):
        self.assertEqual(functions.valid_parentheses("()"), True)
        self.assertEqual(functions.valid_parentheses(")(()))"), False)
        self.assertEqual(functions.valid_parentheses("("), False)
        self.assertEqual(functions.valid_parentheses("(())((()())())"), True)
        self.assertEqual(functions.valid_parentheses('))(('), False)
        self.assertEqual(functions.valid_parentheses('())('), False)
        self.assertEqual(functions.valid_parentheses('()()()()())()('), False)

    def test_three_odd_numbers(self):
        self.assertEqual(functions.three_odd_numbers([1, 2, 3, 4, 5]), True)
        self.assertEqual(functions.three_odd_numbers(
            [0, -2, 4, 1, 9, 12, 4, 1, 0]), True)
        self.assertEqual(functions.three_odd_numbers([5, 2, 1]), False)
        self.assertEqual(functions.three_odd_numbers([1, 2, 3, 3, 2]), False)

    def test_reverse_vowels(self):
        self.assertEqual(functions.reverse_vowels("Hello!"), "Holle!")
        self.assertEqual(functions.reverse_vowels("Tomatoes"), "Temotaos")
        self.assertEqual(functions.reverse_vowels(
            "Reverse Vowels In A String"), "RivArsI Vewols en e Streng")
        self.assertEqual(functions.reverse_vowels("aeiou"), "uoiea")
        self.assertEqual(functions.reverse_vowels(
            "why try, shy fly?"), "why try, shy fly?")


if __name__ == '__main__':
    unittest.main()
