import sys
from collections import deque

def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        operations = sys.stdin.readline().strip()
        n = int(sys.stdin.readline().strip())
        number_list_string = sys.stdin.readline().strip()
        number_list_string = number_list_string[1:-1].split(",")
        if (n != 0):
            number_list = deque([int(num) for num in number_list_string])
        else:
            number_list = deque([])

        is_reversed = False

        next_iter_flag = False
        for i in range(len(operations)):
            if (operations[i] == "D"):
                if (len(number_list) == 0):
                    sys.stdout.write("error\n")
                    next_iter_flag = True
                    break
                else:
                    if is_reversed:
                        number_list.pop()
                    else:
                        number_list.popleft()
            elif (operations[i] == "R"):
                is_reversed = not is_reversed

        if (next_iter_flag):
            continue

        if is_reversed:
            number_list.reverse()

        sys.stdout.write("[" + ",".join(map(str, number_list)) + "]\n")



if __name__ == "__main__":
    Solution()