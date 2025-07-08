import sys

def main():
    input = sys.stdin.readline
    write = sys.stdout.write

    N: int= int(input().strip())

    count = [0] * 10001  # 입력값이 1~10000이므로

    for _ in range(N):
        num = int(input().strip())
        count[num] += 1

    for i in range(1, 10001):
        for _ in range(count[i]):
            write(f"{i}\n")

    pass

if __name__ == "__main__":
    main()
