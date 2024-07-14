import sys
from bisect import bisect_left, bisect_right

def F(prime_list):
    positive_sum = 0
    negative_sum = 0

    for i in range(len(prime_list)):
        if i % 2 == 0:
            positive_sum += prime_list[i]
        else:
            negative_sum += prime_list[i]

    result = 3 * positive_sum - negative_sum

    return result

def actual_code():
    N = int(sys.stdin.readline().strip())

    # 에라토스테네스의 체 적용
    max_limit = 10 ** 5
    prime = [True] * (max_limit + 1)
    i = 2

    while i * i <= max_limit:
        if prime[i]:
            for j in range(i * i, max_limit + 1, i):
                prime[j] = False
        i += 1

    prime_numbers = [i for i in range(2, max_limit + 1) if prime[i]]

    for _ in range(N):
        a, b = map(int, sys.stdin.readline().strip().split())

        start = bisect_left(prime_numbers, a)
        end = bisect_right(prime_numbers, b) - 1

        if start <= end:
            relevant_primes = prime_numbers[start:end + 1]
            result = F(relevant_primes)
        else:
            result = 0

        sys.stdout.write(str(result) + '\n')

if __name__ == '__main__':
    actual_code()
