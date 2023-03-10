def sum_digits(n):
    total_sum = 0
    for i in range(1, n+1):
        digit_sum = sum(int(digit) for digit in str(i))
        total_sum += digit_sum
    return total_sum
    print(sum_digits(5))


def find_max_number(num1,num2,num3):
    max_num=max(num1,num2,num3)
    return max_num
    find_max_number(124,1,2)


def count_even_odd_digits(number):
    number_str = str(number)
    even_count = 0
    odd_count = 0
    for digit_str in number_str:
        digit = int(digit_str)
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count
    even_count, odd_count = count_even_odd_digits(34560)
    print(f"Even digits: {even_count}, Odd digits: {odd_count}")

    def even_integars(even):
        evens_list = []
        for new_list in even:
            if new_list % 2 == 0:
                evens_list.append(new_list)
        return evens_list

    print(even_integars([1, 2, 3, 4]))

#last hmw
#git practice
