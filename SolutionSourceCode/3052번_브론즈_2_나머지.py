import sys

def Solution():
    modulus_set = set()

    for _ in range(10):
        modulus_set.add(int(sys.stdin.readline().strip()) % 42)

    sys.stdout.write(str(len(modulus_set)))

if __name__ == "__main__":
    Solution()