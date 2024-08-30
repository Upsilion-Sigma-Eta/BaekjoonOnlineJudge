import math
import sys

def Solution():
    N = int(sys.stdin.readline().strip())
    problem_input = list(map(int, sys.stdin.readline().strip().split()))

    # 첫 번째 자리의 숫자가 문제의 타입을 결정
    if (problem_input[0] == 1):
        number_arr = [_ for _ in range(1, N + 1)]
        sorted_number_arr = sorted(number_arr)
        result_number_arr = []

        index = 0
        # 0 기반 인덱스로 변경
        target_index = problem_input[1] - 1
        for _ in range(N):
            possible_penumeration_count = math.factorial(len(sorted_number_arr) - 1)
            index = target_index // possible_penumeration_count
            result_number_arr.append(sorted_number_arr.pop(index))
            target_index %= possible_penumeration_count

        sys.stdout.write(" ".join(map(str, result_number_arr)))
    elif (problem_input[0] == 2):
        number_arr = problem_input[1:]

        index = 0
        weight = math.factorial(N - 1)
        sorted_number_arr = sorted(number_arr)
        for number in range(N):
            index += weight * sorted_number_arr.index(number_arr[number])
            sorted_number_arr.remove(number_arr[number])

            if number < N - 1:
                weight //= (N - number - 1)

        sys.stdout.write(str(index + 1))

Solution()