import sys
import itertools


class Picture:
    shape = ""
    background_color = ""
    shape_color = ""

    def __init__(self, _shape, _background_color, _shape_color):
        self.shape = _shape
        self.background_color = _background_color
        self.shape_color = _shape_color


def background_checker(picture_1, picture_2, picture_3):
    if (picture_1.background_color == picture_2.background_color) and \
            (picture_2.background_color == picture_3.background_color) and \
            (picture_1.background_color == picture_3.background_color):
        return True
    elif (picture_1.background_color != picture_2.background_color) and \
            (picture_2.background_color != picture_3.background_color) and \
            (picture_1.background_color != picture_3.background_color):
        return True
    else:
        return False


def shaper_checker(picture_1, picture_2, picture_3):
    if (picture_1.shape == picture_2.shape) and \
            (picture_2.shape == picture_3.shape) and \
            (picture_1.shape == picture_3.shape):
        return True
    elif (picture_1.shape != picture_2.shape) and \
            (picture_2.shape != picture_3.shape) and \
            (picture_1.shape != picture_3.shape):
        return True
    else:
        return False


def shape_color_checker(picture_1, picture_2, picture_3):
    if (picture_1.shape_color == picture_2.shape_color) and \
            (picture_2.shape_color == picture_3.shape_color) and \
            (picture_1.shape_color == picture_2.shape_color):
        return True
    elif (picture_1.shape_color != picture_2.shape_color) and \
            (picture_2.shape_color != picture_3.shape_color) and \
            (picture_1.shape_color != picture_3.shape_color):
        return True
    else:
        return False


def Solution():
    pictures = list()

    for i in range(9):
        shape, background_color, shape_color = sys.stdin.readline().strip().split()
        pictures.append(Picture(shape, background_color, shape_color))

    game_counter = int(sys.stdin.readline().strip())
    score_counter = 0
    total_picture_combination = itertools.combinations(range(1, 10), 3)

    already_said_set = set()
    answer_set = set()
    is_G_called = False

    for comb in total_picture_combination:
        if (background_checker(pictures[comb[0] - 1], pictures[comb[1] - 1], pictures[comb[2] - 1]) and \
                shaper_checker(pictures[comb[0] - 1], pictures[comb[1] - 1], pictures[comb[2] - 1]) and \
                shape_color_checker(pictures[comb[0] - 1], pictures[comb[1] - 1], pictures[comb[2] - 1])):
            answer_set.add((comb[0], comb[1], comb[2]))

    for i in range(game_counter):
        parameter = list(sys.stdin.readline().strip().split())

        if (parameter[0] == "H"):
            parameter_picture_index = [int(parameter[1]), int(parameter[2]), int(parameter[3])]

            parameter_picture_index.sort()

            parameter_picture_index_tuple = tuple(parameter_picture_index)

            if (parameter_picture_index_tuple) in answer_set:
                if (parameter_picture_index_tuple not in already_said_set):
                    score_counter += 1
                    already_said_set.add(parameter_picture_index_tuple)
                    answer_set.remove(parameter_picture_index_tuple)
                else:
                    score_counter -= 1
            else:
                score_counter -= 1
        else:
            if len(answer_set) != 0 or is_G_called:
                score_counter -= 1
            else:
                score_counter += 3
                is_G_called = True

    sys.stdout.write(str(score_counter))


if __name__ == "__main__":
    Solution()