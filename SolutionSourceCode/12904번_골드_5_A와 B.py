import sys

def Solution():
    S = list(sys.stdin.readline().strip())
    T = list(sys.stdin.readline().strip())

    while len(T) > len(S):
        if (T[-1] == "A"):
            T = T[:-1]
        elif T[-1] == "B":
            T = T[:-1]
            T.reverse()

    S_string = "".join(S)
    T_string = "".join(T)

    if (S_string == T_string):
        sys.stdout.write("1")
    else:
        sys.stdout.write("0")


if __name__ == "__main__":
    Solution()