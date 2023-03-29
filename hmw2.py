#TODO
# Enumerate All Primes To N
# Write a program that takes an integer argument and returns all the primes between 1 and that integer.
# For example, if the input is 18, you should return [2, 3, 5, 7, 11, 13, 17].
# A natural number is called a prime if it is bigger than 1 and has no divisors other than 1 and itself.

def get_primes(n):
    primes = []
    for i in range(2, n+1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


print(get_primes(18))


#TODO
# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]


def reorder_list(lst):
    even_idx = 0
    odd_idx = len(lst) - 1

    while even_idx < odd_idx:
        if lst[even_idx] % 2 == 0:
            even_idx += 1
        else:
            lst[even_idx], lst[odd_idx] = lst[odd_idx], lst[even_idx]
            odd_idx -= 1

    return lst


lst = [7, 3, 5, 6, 4, 10, 3, 2]
print(reorder_list(lst))


#TODO
# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative
# decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].

def increment_digits(digits):
    n = len(digits)
    for i in range(n-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits
    digits.insert(0, 1)
    return digits


digits = [1, 2, 9]
incremented_digits = increment_digits(digits)
print(incremented_digits)


#TODO
# Complete the solution so that it returns true if the first argument(string)
# passed in ends with the 2nd argument (also a string).
# Examples:
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false


def solution(string, ending):
    return string[-len(ending):] == ending


