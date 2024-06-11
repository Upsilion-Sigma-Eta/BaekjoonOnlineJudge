import sys

def actual_code():
    total_day_number = int(sys.stdin.readline().strip())

    for i in range(1, total_day_number + 1):
        header_info = sys.stdin.readline().strip()
        path_state = sys.stdin.readline().strip()

        sys.stdout.write('Day #' + str(i) + '\n')
        sys.stdout.write(header_info + '\n')
        sys.stdout.write(path_state + '\n')

        total_cell = int(header_info.split(' ')[0])
        maximum_jump_length = int(header_info.split(' ')[1])

        current_jump_count = 0
        current_target_pos = min(total_cell - 1, maximum_jump_length + 1)
        current_pos = 0

        if (current_target_pos == total_cell - 1):
            sys.stdout.write('1\n\n')
            continue

        while (current_pos < total_cell - 1):
            if (path_state[current_target_pos] == 'X'):
                current_target_pos -= 1

                if (current_target_pos <= current_pos):
                    current_jump_count = 0
                    break
            else:
                current_jump_count += 1
                current_pos = current_target_pos
                current_target_pos = min(total_cell - 1, current_target_pos + maximum_jump_length + 1)

        if (i == total_day_number):
            sys.stdout.write(str(current_jump_count))
        else:
            sys.stdout.write(str(current_jump_count) + '\n\n')

if __name__ == '__main__':
    actual_code()
