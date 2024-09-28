import sys
import math

def Solution():
    N = int(sys.stdin.readline().strip())
    number_list = list(map(int, sys.stdin.readline().strip().split()))

    primer_number_counter = 0
    for number in number_list:
        if (number == 1):
            continue

        is_prime_number_flag = True
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                is_prime_number_flag = False
                break

        if is_prime_number_flag:
            primer_number_counter += 1

    sys.stdout.write(str(primer_number_counter))

if __name__ == "__main__":
    Solution()