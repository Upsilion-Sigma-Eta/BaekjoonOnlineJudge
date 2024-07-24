import sys

move_number = 0
move_order = []

def hanoi(n, from_, to, via):
    global move_number
    global move_order

    if n == 1:
        move_number += 1
        move_order.append((from_, to))
    else:
        hanoi(n - 1, from_, via, to)
        move_number += 1
        move_order.append((from_, to))
        hanoi(n - 1, via, to, from_)

def actual_code():
    N = int(sys.stdin.readline().strip())

    hanoi(N, 1, 3, 2)

    sys.stdout.write(str(move_number) + '\n')
    for move in move_order:
        sys.stdout.write(str(move[0]) + " " + str(move[1]) + '\n')


if __name__ == '__main__':
    actual_code()
