import sys
import math

def actual_code():
    v, k = map(int, sys.stdin.readline().split())

    votes = []
    current_vote = v
    while current_vote > 0:
        # Add k values
        for i in range(k):
            if current_vote > 0:
                votes.append(current_vote)
                current_vote -= 1

        # Skip next k values
        current_vote -= k

    sys.stdout.write(str(len(votes)) + '\n')
    for vote in votes:
        sys.stdout.write(str(vote) + '\n')

if __name__ == '__main__':
    actual_code()