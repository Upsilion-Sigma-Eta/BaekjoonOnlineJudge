import sys

def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        answer_sheet = sys.stdin.readline().strip()

        score = 0
        current_combo = 1
        for answer in answer_sheet:
            if answer == "X":
                current_combo = 1
            else:
                score += current_combo
                current_combo += 1

        sys.stdout.write(f"{score}\n")

if __name__ == "__main__":
    Solution()