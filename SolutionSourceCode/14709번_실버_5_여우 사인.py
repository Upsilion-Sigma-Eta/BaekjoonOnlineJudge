import sys

def actual_code():
    test_case_number = int(sys.stdin.readline().strip())

    finger_pair_list = []
    for i in range(test_case_number):
        finger_pair_list.append(list(map(int, sys.stdin.readline().strip().split(' '))))

    is_fox_sign = False

    first_third_connect = False
    fourth_third_connect = False
    first_fourth_connect = False
    second_is_free = True
    fifth_is_free = True
    for finger_pair in finger_pair_list:
        if (finger_pair[0] == 1 and finger_pair[1] == 3) or (finger_pair[0] == 3 and finger_pair[1] == 1):
            first_third_connect = True
        elif (finger_pair[0] == 4 and finger_pair[1] == 3) or (finger_pair[0] == 3 and finger_pair[1] == 4):
            fourth_third_connect = True
        elif (finger_pair[0] == 1 and finger_pair[1] == 4) or (finger_pair[0] == 4 and finger_pair[1] == 1):
            first_fourth_connect = True
        elif finger_pair[0] == 2 or finger_pair[1] == 2:
            second_is_free = False
        elif finger_pair[0] == 5 or finger_pair[1] == 5:
            fifth_is_free = False


    if first_third_connect and fourth_third_connect and first_fourth_connect and second_is_free and fifth_is_free:
        is_fox_sign = True

    if (is_fox_sign):
        sys.stdout.write("Wa-pa-pa-pa-pa-pa-pow!")
    else:
        sys.stdout.write("Woof-meow-tweet-squeek")

if __name__ == '__main__':
    actual_code()
