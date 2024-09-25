import sys

def Solution():
    S = sys.stdin.readline().strip()

    for i in range(ord("z") - ord("a") + 1):
        sys.stdout.write(f"{S.find(chr(ord('a') + i))} ")

if __name__ == "__main__":
    Solution()