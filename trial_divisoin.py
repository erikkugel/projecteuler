#!/usr/bin/python
#
# Ernest Kugel, Oct. 2013
#
# Poject Eurler, Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.


# Test a prime number using Trial Division (http://en.wikipedia.org/wiki/Trial_division)
def is_prime_trial_division (number):
	if number <= 2:
		return false
	import math
	max_prime = math.sqrt(number)
	test = 2
	while number % test != 0:
		if test > max_prime:
			return True
		test = test + 1
	return False

total = 0
for next_number in (3..1000):
	if is_prime_trial_division (next_number) total = total + next_number
