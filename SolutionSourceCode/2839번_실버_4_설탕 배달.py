import sys

def actual_code():
    total_sugar_amount = int(sys.stdin.readline().strip())

    sugar_remaining = total_sugar_amount

    five_kilo_amount = 0
    three_kilo_amount = 0

    five_kilo_amount = sugar_remaining // 5

    sugar_remaining -= five_kilo_amount * 5

    three_kilo_amount = sugar_remaining // 3

    sugar_remaining -= three_kilo_amount * 3

    while (sugar_remaining > 0):
        five_kilo_amount -= 1
        sugar_remaining += 5
        three_kilo_amount += sugar_remaining // 3
        sugar_remaining -= (sugar_remaining // 3) * 3

        if (five_kilo_amount < 0):
            sys.stdout.write("-1")
            return

    sys.stdout.write(str(five_kilo_amount + three_kilo_amount))

if __name__ == '__main__':
    actual_code()
