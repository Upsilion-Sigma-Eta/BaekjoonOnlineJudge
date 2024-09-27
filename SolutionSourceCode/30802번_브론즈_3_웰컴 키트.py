import sys
import math

def Solution():
    N = int(sys.stdin.readline().strip())

    S, M, L, XL, XXL, XXXL = map(int, sys.stdin.readline().strip().split())

    T, P = map(int, sys.stdin.readline().strip().split())

    t_shirt_order_list = [math.ceil(S / T), math.ceil(M / T), math.ceil(L / T), math.ceil(XL / T), math.ceil(XXL / T), math.ceil(XXXL / T)]
    t_shirt_order_count = sum(t_shirt_order_list)
    t_shirt_order_count = int(t_shirt_order_count)

    pen_order_count = N // P
    pen_order_single_count = N % P

    sys.stdout.write(f"{t_shirt_order_count}\n")
    sys.stdout.write(f"{pen_order_count} {pen_order_single_count}\n")

if __name__ == "__main__":
    Solution()