import sys

def F(n):
    str_new = ""
    for digit in str(n):
        str_new += str(9 - int(digit))

    return int(str_new)

def most_nearest_max_digit_number(n):
    n_str = str(n)
    length = len(n_str)

    max_number = "4"

    for i in range(length - 1):
        max_number += '9'

    return int(max_number)

def actual_code():
    test_case_number = int(sys.stdin.readline().strip())

    for _ in range(test_case_number):
        number_range_max = int(sys.stdin.readline().strip())

        max_value = 0

        candidate_1 = most_nearest_max_digit_number(number_range_max)

        while candidate_1 > number_range_max:
            candidate_1 = number_range_max

        max_value = candidate_1 * F(candidate_1)

        sys.stdout.write(str(max_value) + '\n')


if __name__ == '__main__':
    actual_code()
