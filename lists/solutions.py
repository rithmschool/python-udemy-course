# 1

answer = [person[0] for person in ["Elie", "Tim", "Matt"]]

answer2 = [val for val in [1, 2, 3, 4, 5, 6] if val % 2 == 0]

# 2

answer = [val for val in [1, 2, 3, 4] if val in [3, 4, 5, 6]]

answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

# 3

answer = [val for val in range(0, 101) if val % 12 == 0]

# 4

answer = [char for char in "amazing" if char not in "aeiou"]

# 5

answer = [[i for i in range(0, 3)] for num in range(0, 3)]

#

answer = [[i for i in range(0, 10)] for num in range(0, 10)]
