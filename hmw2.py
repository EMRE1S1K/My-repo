# def sum_digits(n):
#     total_sum = 0
#     for i in range(1, n+1):
#         digit_sum = sum(int(digit) for digit in str(i))
#         total_sum += digit_sum
#     return total_sum
#     print(sum_digits(5))
#
#
# def find_max_number(num1,num2,num3):
#     max_num=max(num1,num2,num3)
#     return max_num
#     find_max_number(124,1,2)
#
#
# def count_even_odd_digits(number):
#     number_str = str(number)
#     even_count = 0
#     odd_count = 0
#     for digit_str in number_str:
#         digit = int(digit_str)
#         if digit % 2 == 0:
#             even_count += 1
#         else:
#             odd_count += 1
#     return even_count, odd_count
#     even_count, odd_count = count_even_odd_digits(34560)
#     print(f"Even digits: {even_count}, Odd digits: {odd_count}")
#
#     def even_integars(even):
#         evens_list = []
#         for new_list in even:
#             if new_list % 2 == 0:
#                 evens_list.append(new_list)
#         return evens_list
#
#     print(even_integars([1, 2, 3, 4]))
#
# #last hmw
# #git practice
#
# def descending_order(num):
#     # Convert the number to a string and split it into a list of digits
#     digits = list(str(num))
#
#     # Sort the digits in descending order
#     digits.sort(reverse=True)
#
#     # Join the digits back together into a string and convert back to an integer
#     result = int(''.join(digits))
#
#     return result
#
# num = 123456789
# result = descending_order(num)
# print(result)  # Output: 987654321


# def factorial(n: int):
#     result = 1
#     for i in range(2, n+1):
#         result = result * i
#
#
# number = 5
# factorial(number)

#Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.


from collections import Counter

def frequency_sort(s):
    char_count = Counter(s)
    sorted_chars = sorted(char_count, key=lambda x: char_count[x], reverse=True)
    return "".join([c * char_count[c] for c in sorted_chars])


s = "abcabcaba"
result = frequency_sort(s)
print(result)

# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.

def unique_char(n):
    seen_char = set()
    for char in n:
        if char in seen_char:
            return False
        seen_char.add(char)
    return True


print(unique_char('abcd'))
print(unique_char('aabcde'))


