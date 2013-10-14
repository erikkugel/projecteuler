#!/usr/bin/python
#
# Ernest Kugel, Oct. 2013.
#
# Project Euler (http://projecteuler.net/), Problem 3

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import math

# Test a prime number using Trial Division (http://en.wikipedia.org/wiki/Trial_division)
def is_prime_trial_division (number):
	if number <= 2:
		return False
	max_prime = math.sqrt(number)
	test = 2
	while number % test != 0:
		if test > max_prime:
			return True
		test += 1
	return False

largest_prime = int(math.sqrt(600851475143))
while largest_prime > 2:
	if is_prime_trial_division(largest_prime) and 600851475143 % largest_prime == 0:
		print largest_prime
		break
	largest_prime -= 1
