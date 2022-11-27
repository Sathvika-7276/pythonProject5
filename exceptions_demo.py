"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When the value entered is not an integer or any value other than integer.
2. When will a ZeroDivisionError occur? When denominator is zero.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, by using while loop as a check.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Error")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
# except ZeroDivisionError:
    # print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur? When the numerator or denominator are not integers.
# When will a ZeroDivisionError occur? When the denominator value is zero.
# Could you change the code to avoid the possibility of a ZeroDivisionError? Yes, using while loop check conditions.

# If you could figure out the answer to question 3, then make this change now.
