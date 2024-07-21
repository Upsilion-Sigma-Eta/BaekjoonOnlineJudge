import sys

def actual_code():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    pos_3 = int(a) * int(b[2])
    pos_4 = int(a) * int(b[1])
    pos_5 = int(a) * int(b[0])
    pos_6 = int(a) * int(b)

    sys.stdout.write(str(pos_3) + "\n")
    sys.stdout.write(str(pos_4) + "\n")
    sys.stdout.write(str(pos_5) + "\n")
    sys.stdout.write(str(pos_6) + "\n")

if __name__ == '__main__':
    actual_code()
