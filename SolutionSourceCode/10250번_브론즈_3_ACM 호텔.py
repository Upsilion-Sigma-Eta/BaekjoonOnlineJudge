import sys

def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        H, W, N = map(int, sys.stdin.readline().strip().split())

        floor_number = (N % H)
        room_number = (N // H + 1)

        if floor_number == 0:
            floor_number = H
            room_number -= 1

        sys.stdout.write(str(floor_number) + f"{room_number:02d}\n")

if __name__ == "__main__":
    Solution()
