import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3

# What did you see on line 1? Integer value between 5 and 20 where 5 and 20 is inclusive.
# What was the smallest number you could have seen, what was the largest? smallest is 5 and largest is 20.

# What did you see on line 2? Integer value from 3 to 10 with a step value 2, 3 is inclusive but 10 is not.
# What was the smallest number you could have seen, what was the largest? smallest is 3 and largest is 9.
# Could line 2 have produced a 4? No,cause 2 is the step value and the next value of 3 is 5.

# What did you see on line 3? A float value in range of 2.5 and 5.5 where 2.5 and 5.5 is inclusive.
# What was the smallest number you could have seen, what was the largest? Smallest number is 2.5 and largest is 5.5

# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
print(random.randint(1, 100))
