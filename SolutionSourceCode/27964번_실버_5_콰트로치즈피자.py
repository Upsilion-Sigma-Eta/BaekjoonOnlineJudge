import sys

def actual_code():
    N = int(sys.stdin.readline().strip())

    toping_set = set()

    toping_list = list(sys.stdin.readline().strip().split())

    for toping in toping_list:
        toping_set.add(toping)

    cheese_amount = 0
    for toping in toping_set:
        if (len(toping) >= 6):
            if (toping[-6:] == "Cheese"):
                cheese_amount += 1
        if (cheese_amount >= 4):
            sys.stdout.write("yummy\n")
            return

    sys.stdout.write("sad\n")

if __name__ == '__main__':
    actual_code()