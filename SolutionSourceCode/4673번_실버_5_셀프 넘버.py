import sys

def d(n):
    n_str = str(n)

    for digit in n_str:
        n += int(digit)

    return n

def actual_code():

    self_number_list = []
    for i in range(10000):
        self_number_list.append(i)

    for i in range(0, 10000, 1):
        if d(i) in self_number_list:
            self_number_list.remove(d(i))

    for i in self_number_list:
        sys.stdout.write(str(i) + '\n')


if __name__ == '__main__':
    actual_code()
