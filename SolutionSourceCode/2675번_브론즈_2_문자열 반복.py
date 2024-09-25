import sys

def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        R, S = sys.stdin.readline().strip().split()
        R = int(R)

        result_string = ""
        for idx in range(len(S)):
            result_string += S[idx] * R

        sys.stdout.write(result_string + "\n")


if __name__ == "__main__":
    Solution()