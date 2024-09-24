import sys

def Solution():
    N = int(sys.stdin.readline().strip())
    N_list =  list(map(int, sys.stdin.readline().strip().split()))

    sys.stdout.write(str(min(N_list)) + " " + str(max(N_list)))

if __name__ == "__main__":
    Solution()
