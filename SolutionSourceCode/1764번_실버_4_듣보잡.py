import sys

def actual_code():
    N, M = map(int, sys.stdin.readline().split())

    no_heard = set()
    no_seen = set()

    for _ in range(N):
        no_heard.add(sys.stdin.readline().strip())

    for _ in range(M):
        no_seen.add(sys.stdin.readline().strip())

    no_heard_or_seen = list(no_heard.intersection(no_seen))
    no_heard_or_seen.sort()

    sys.stdout.write(str(len(no_heard_or_seen)) + '\n')

    for i in range(len(no_heard_or_seen)):
        sys.stdout.write(no_heard_or_seen[i] + '\n')

if __name__ == '__main__':
    actual_code()
