import sys

def Solution():
    N = int(sys.stdin.readline().strip())

    current_string_history = []
    current_string = ""

    for _ in range(N):
        has_time_save_point = False

        operation, command, time = sys.stdin.readline().strip().split()
        time = int(time)

        if operation == "type":
            current_string += command
            current_string_history.append((current_string, time))
        elif (operation == "undo"):
            undo_time = time - int(command)

            for i in range(len(current_string_history) - 1, -1, -1):
                if current_string_history[i][1] < undo_time:
                    has_time_save_point = True
                    current_string = current_string_history[i][0]
                    current_string_history.append((current_string, time))
                    break
            if not has_time_save_point:
                current_string = ""
                current_string_history.append((current_string, time))


    sys.stdout.write(current_string_history[-1][0])

if __name__ == "__main__":
    Solution()