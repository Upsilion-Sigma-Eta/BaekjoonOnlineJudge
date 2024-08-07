import sys


def sorting(N, arr, S):
    swap_counter = S
    start = 0
    while swap_counter > 0:
        sliced_arr = arr[start:start + swap_counter + 1]

        if (sliced_arr == []):
            return

        max_value_index = arr.index(max(sliced_arr))
        for j in range(max_value_index, 0, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                swap_counter -= 1

                if (swap_counter <= 0):
                    return

        start += 1

def Solution():
    N = int(sys.stdin.readline().strip())

    arr = list(map(int, sys.stdin.readline().strip().split()))

    S = int(sys.stdin.readline().strip())

    sorting(N, arr, S)

    for i in range(N):
        sys.stdout.write(str(arr[i]) + " ")

if __name__ == "__main__":
    Solution()