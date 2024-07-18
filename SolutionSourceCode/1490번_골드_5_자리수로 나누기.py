import sys

def number_string_generator(string_N_List, N):


    number_postfix = []

    string_number_to_test = ''.join(string_N_List)

    for i in range(len(number_postfix) - 1, -1, -1):
        if (number_postfix[i] >= 10):
            if (i - 1 >= 0):
                number_postfix[i - 1] += 1
                number_postfix[i] = 0
            else:
                number_postfix.insert(0, 0)

    postfix_string = ''
    for digit in number_postfix:
        postfix_string += str(digit)

    string_number_to_test += (postfix_string)

    is_answer = True
    for digit in string_N_List:
        if not string_integer_mod_is_zero(string_number_to_test, int(digit)):
            is_answer = False
            break

    if is_answer:
        return string_number_to_test



    number_postfix = [0]

    while (True):
        string_number_to_test = ''.join(string_N_List)

        for i in range(len(number_postfix) - 1, -1, -1):
            if (number_postfix[i] >= 10):
                if (i - 1 >= 0):
                    number_postfix[i - 1] += 1
                    number_postfix[i] = 0
                else:
                    number_postfix.insert(0, 0)
                    number_postfix[i + 1] = 0

        postfix_string = ''
        for digit in number_postfix:
            postfix_string += str(digit)

        string_number_to_test += (postfix_string)

        is_answer = True
        for digit in string_N_List:
            if not string_integer_mod_is_zero(string_number_to_test, int(digit)):
                is_answer = False
                break

        if is_answer:
            return string_number_to_test

        number_postfix[-1] += 1


def string_integer_mod_is_zero(string, mod):
    if (mod == 0):
        return True
    return int(string) % mod == 0

def actual_code():
    N = int(sys.stdin.readline().strip())

    string_N = str(N)

    string_N_List = list(string_N)

    result = number_string_generator(string_N_List, N)

    sys.stdout.write(result)

if __name__ == '__main__':
    actual_code()
