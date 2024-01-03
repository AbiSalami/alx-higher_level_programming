#!/usr/bin/python3
"""print all possiblee different combinations of two digits in ascending order.
  The two digits must be different - 01 and 10 are considered identical.
  """
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        if digit1 == 6 and digit2 == 7:
            print("{}{}".format(digit1, digit2))
        else:
            print("{}{}".format(digit1, digit2), end=", ")
