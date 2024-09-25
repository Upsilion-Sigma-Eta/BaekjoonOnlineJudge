import sys

def Solution():
    number_list = list(map(int, sys.stdin.readline().strip().split()))

    number_list_ascend = sorted(number_list, reverse=False)
    number_list_descend = sorted(number_list, reverse=True)

    if (number_list == number_list_descend):
        print("descending")
    elif (number_list == number_list_ascend):
        print("ascending")
    else:
        print("mixed")


if __name__ == "__main__":
    Solution()