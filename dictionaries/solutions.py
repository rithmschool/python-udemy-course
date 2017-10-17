# 1

instructor = {
  "name": "Colt",
  "owns_dog": True,
  "owns_cat": True,
  "owns_fish": False,
  "owns_hamster": False
}

list_of_keys = ['name', 'owns_dog', 'owns_cat', 'owns_fish', 'owns_hamster']

list(instructor.keys()) # ['name', 'owns_dog', 'owns_cat', 'owns_fish', 'owns_hamster']
# 2

instructor = {
  "name": "Colt",
  "owns_dog": True,
  "owns_cat": True,
  "owns_fish": False,
  "owns_hamster": False
}

list_of_values = ['name', 'owns_dog', 'owns_cat', 'owns_fish', 'owns_hamster']

list(instructor.values()) # ['Colt', True, True, False, False]

# 3

answer = {val[0]:val[1] for val in [["name", "Colt"], ["job", "Instructor"]]}

# 4

l = ["CA", "NJ", "RI"]
l2 = ["California", "New Jersey", "Rhode Island"]

answer = {l2[i]: l[i] for i in range(0,3)}

# 5

answer = {char:0 for char in ["a","e","i","o","u"]}

# 6

answer = {(count-64): chr(count) for count in range(65,91)}

# 7

string = "awesome sauce"

answer = {vowel: string.count(vowel) for vowel in "awesome sauce" if vowel in "aeiou"}
