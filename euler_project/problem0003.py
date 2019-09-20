'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143
'''
import math

composite_number = 600851475143
sqrt_composite = math.sqrt(composite_number)
possible_divisor = 2

while possible_divisor <= sqrt_composite:
    if composite_number % possible_divisor == 0:
        composite_number = composite_number / possible_divisor
        sqrt_composite = math.sqrt(composite_number)
    else:
        possible_divisor += 1
print(composite_number)