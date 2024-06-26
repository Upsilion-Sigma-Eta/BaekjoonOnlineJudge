import sys
import math

RIGHT = (1, 0)
LEFT = (-1, 0)
UP = (0, -1)
DOWN = (0, 1)
CENTER = (0, 0)
global N

def get_left_coord(x, y):
    left_coord = [x + LEFT[0], y + LEFT[1]]
    left_coord[0] = max(min(left_coord[0], N - 1), 0)
    left_coord[1] = max(min(left_coord[1], N - 1), 0)

    return left_coord

def get_right_coord(x, y):
    right_coord = [x + RIGHT[0], y + RIGHT[1]]
    right_coord[0] = max(min(right_coord[0], N - 1), 0)
    right_coord[1] = max(min(right_coord[1], N - 1), 0)

    return right_coord

def get_up_coord(x, y):
    up_coord = [x + UP[0], y + UP[1]]
    up_coord[0] = max(min(up_coord[0], N - 1), 0)
    up_coord[1] = max(min(up_coord[1], N - 1), 0)

    return up_coord

def get_down_coord(x, y):
    down_coord = [x + DOWN[0], y + DOWN[1]]
    down_coord[0] = max(min(down_coord[0], N - 1), 0)
    down_coord[1] = max(min(down_coord[1], N - 1), 0)

    return down_coord

def get_nearby_empty_seats(classroom, x, y):
    empty_seats_coord = [get_left_coord(x, y), get_up_coord(x, y), get_down_coord(x, y), get_right_coord(x, y)]

    empty_seats_coord = list(filter(lambda coord: classroom[coord[0]][coord[1]] == -1 and not(coord[0] == x and coord[1] == y), empty_seats_coord))

    return empty_seats_coord

def get_nearby_student_seats(classroom, x, y):
    student_seats_coord = [get_left_coord(x, y), get_up_coord(x, y), get_down_coord(x, y), get_right_coord(x, y)]

    student_seats_coord = list(filter(lambda coord: classroom[coord[0]][coord[1]] != -1 and not(coord[0] == x and coord[1] == y), student_seats_coord))

    return student_seats_coord

def get_nearby_favorite_student_seats(classroom, x, y, favorite_students):
    favorite_student_seats = []
    student_seats = get_nearby_student_seats(classroom, x, y)

    for student_seat in student_seats:
        if (classroom[student_seat[0]][student_seat[1]] in favorite_students):
            favorite_student_seats.append(student_seat)

    return favorite_student_seats

def get_nearby_favorite_student_count(classroom, x, y, favorite_students):
    favorite_student_seats = get_nearby_favorite_student_seats(classroom, x, y, favorite_students)

    return len(favorite_student_seats)

def get_nearby_empty_seats_count(classroom, x, y):
    empty_seats = get_nearby_empty_seats(classroom, x, y)

    return len(empty_seats)

def actual_code():
    global N
    N = int(sys.stdin.readline().strip())

    classroom = []
    student_coord_dict = {}

    for _ in range(N):
        classroom.append([-1 for _ in range(N)])

    studentArr = []
    for _ in range(N):
        for __ in range(N):
            student = tuple(map(int, sys.stdin.readline().strip().split()))
            studentArr.append((student[0], [student[1], student[2], student[3], student[4]]))

    classroom[1][1] = studentArr[0][0]
    student_coord_dict[studentArr[0][0]] = (1, 1)

    for student_index in range(1, len(studentArr)):
        student = studentArr[student_index]
        first_candidate_seat = []
        second_candidate_seat = []
        for i in range(0, N):
            for j in range(0, N):
                if (classroom[i][j] == -1):
                    first_candidate_seat.append((get_nearby_favorite_student_count(classroom, i, j, student[1]), (i, j)))

        first_candidate_seat.sort(key=lambda x: x[0], reverse=True)

        max_ff_student_count = max(first_candidate_seat, key=lambda x: x[0])[0]

        first_candidate_seat = list(filter(lambda x: x[0] == max_ff_student_count, first_candidate_seat))

        if (len(first_candidate_seat) > 1):
            for seat in first_candidate_seat:
                second_candidate_seat.append((get_nearby_empty_seats_count(classroom, seat[1][0], seat[1][1]), seat[1]))

            second_candidate_seat.sort(key=lambda x: x[0], reverse=True)

            max_es_count = max(second_candidate_seat, key=lambda x : x[0])[0]

            second_candidate_seat = list(filter(lambda x: x[0] == max_es_count, second_candidate_seat))

            if (len(second_candidate_seat) > 1):
                second_candidate_seat = sorted(second_candidate_seat, key=lambda x: (x[1][0], x[1][1]))
                classroom[second_candidate_seat[0][1][0]][second_candidate_seat[0][1][1]] = student[0]
                student_coord_dict[student[0]] = (second_candidate_seat[0][1][0], second_candidate_seat[0][1][1])
            else:
                classroom[second_candidate_seat[0][1][0]][second_candidate_seat[0][1][1]] = student[0]
                student_coord_dict[student[0]] = (second_candidate_seat[0][1][0], second_candidate_seat[0][1][1])
        else:
            classroom[first_candidate_seat[0][1][0]][first_candidate_seat[0][1][1]] = student[0]
            student_coord_dict[student[0]] = (first_candidate_seat[0][1][0], first_candidate_seat[0][1][1])

    likeness_total = 0
    for (student_index) in student_coord_dict.keys():
            studentArr.sort(key=lambda x: x[0])
            nearby_ff_number = get_nearby_favorite_student_count(classroom, student_coord_dict[student_index][0], student_coord_dict[student_index][1], studentArr[student_index - 1][1])

            if (nearby_ff_number == 0):
                likeness_total += 0
            elif (nearby_ff_number == 1):
                likeness_total += 1
            else:
                likeness_total += 10 ** (nearby_ff_number - 1)

    sys.stdout.write(str(likeness_total) + "\n")



if __name__ == '__main__':
    actual_code()