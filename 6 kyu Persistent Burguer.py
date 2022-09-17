# This Kata can be found at https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec
#
# Description:
#
# Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.
# For example (Input --> Output):
# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
# 4 --> 0 (because 4 is already a one-digit number)
#
# Solution:

def persistence(n):
    mult_persistence = 0
    calculate = n
    if len(str(n)) == 1:
        return 0
    while 1:
        sumed = 1
        for value in str(calculate):
            sumed *= int(value)
        mult_persistence += 1
        calculate = sumed
        if len(str(calculate)) == 1:
            return mult_persistence
            break
