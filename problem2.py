#!/usr/bin/python
#
# Ernest Kugel, Oct. 2013.
#
# Project Euler (http://projecteuler.net/), Problem 2

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.


n1 = 1
n2 = 2
ceiling = 4000000

total = 0
while n2 <= ceiling:
	if n2 % 2 == 0:
		total += n2
	tmp = n2
	n2 += n1
	n1 = tmp

print total
