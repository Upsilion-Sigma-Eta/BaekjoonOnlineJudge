import sys

def Solution():
    A = int(sys.stdin.readline().strip())
    B = int(sys.stdin.readline().strip())
    C = int(sys.stdin.readline().strip())

    multiplied_number = str(A * B * C)

    number_appear_list = [0 for _ in range(10)]

    for digit in multiplied_number:
        number_appear_list[int(digit)] += 1

    for i in range(len(number_appear_list)):
        sys.stdout.write(str(number_appear_list[i]) + "\n")

if __name__ == "__main__":
    Solution()
