import sys
import copy

def rotate_right_45degree(array):
    new_array = copy.deepcopy(array)

    row_count = len(array)
    row_count -= 1
    
    # 중앙 열
    for i in range(row_count + 1):
        new_array[i][(row_count + 1) // 2] = array[i][i]

    # 반 대각선
    for i in range(row_count + 1):
        new_array[i][row_count - i] = array[i][(row_count + 1) // 2]

    # 중앙 행
    for i in range(row_count + 1):
        new_array[(row_count + 1) // 2][row_count - i] = array[i][row_count - i]

    # 대각선
    for i in range(row_count + 1):
        new_array[i][i] = array[(row_count + 1) // 2][i]

    return new_array

def rotate_left_45degree(array):
    new_array = copy.deepcopy(array)

    row_count = len(array)
    row_count -= 1
    
    # 중앙 열
    for i in range(row_count + 1):
        new_array[i][(row_count + 1) // 2] = array[i][row_count - i]

    # 반 대각선
    for i in range(row_count + 1):
        new_array[i][row_count - i] = array[(row_count + 1) // 2][row_count - i]

    # 중앙 행
    for i in range(row_count + 1):
        new_array[(row_count + 1) // 2][i] = array[i][i]

    # 대각선
    for i in range(row_count + 1):
        new_array[i][i] = array[i][(row_count + 1) // 2]

    return new_array

def actual_code():
    test_case_number = int(sys.stdin.readline().strip())

    for i in range(test_case_number):
        array_size, rotation_degree = map(int, sys.stdin.readline().strip().split(' '))

        original_array = []

        for j in range(array_size):
            original_array.append(sys.stdin.readline().strip().split(' '))

        if rotation_degree > 0:
            for j in range(rotation_degree // 45):
                original_array = rotate_right_45degree(original_array)
        elif rotation_degree < 0:
            for j in range(abs(rotation_degree) // 45):
                original_array = rotate_left_45degree(original_array)

        for j in range(array_size):
            for k in range(array_size):
                sys.stdout.write(original_array[j][k] + ' ')
            sys.stdout.write('\n')



if __name__ == '__main__':
    actual_code()
