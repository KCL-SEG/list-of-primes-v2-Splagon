"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
import pytest

def primes(number_of_primes):
    list = []

    if (number_of_primes < 1):
        raise ValueError("There must be a positive number of primes")
    else:
        i = 2   #current number checking if prime; and 1 isn't prime
        currentNumberOfPrimes = 0;
        while (currentNumberOfPrimes < number_of_primes):
            numberOfFactors = 2; #every number is divisible by 1 and itself
            for n in list:
                if (i % n == 0):
                    numberOfFactors += 1
                    break
            if(numberOfFactors == 2):
                list.append(i)
                currentNumberOfPrimes += 1
            i += 1
    return list
