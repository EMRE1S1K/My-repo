# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below
# the original list’s arithmetical mean. The arithmetical mean is the sum of
# all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]
#
# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3


def below_mean(lst):
    mean = sum(lst) / len(lst)
    return [num for num in lst if num < mean]


input_list = [1, 3, 5, 6, 4, 10, 2, 3]
output_list = below_mean(input_list)
print(output_list)


def lowest_element(list_2):
    sorted_list = sorted(list_2)
    return sorted_list[:2]


example = [198, 3, 4, 9, 10, 9, 2]
print(lowest_element(example))

