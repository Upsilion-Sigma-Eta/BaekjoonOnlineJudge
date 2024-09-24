import sys

def Solution():
    word_list = sys.stdin.readline().strip()

    sys.stdout.write(str(len(word_list.split())))

if __name__ == "__main__":
    Solution()
