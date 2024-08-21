import sys

def Solution():

    while True:
        m = int(sys.stdin.readline().strip())

        if (m == 0):
            return

        sentence = sys.stdin.readline().strip()

        char_count_map = {}
        left = 0
        max_length = 0

        for right in range(len(sentence)):
            if sentence[right] in char_count_map:
                char_count_map[sentence[right]] += 1
            else:
                char_count_map[sentence[right]] = 1

            while len(char_count_map) > m:
                char_count_map[sentence[left]] -= 1
                if (char_count_map[sentence[left]] == 0):
                    del char_count_map[sentence[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        sys.stdout.write(str(max_length) + "\n")

if __name__ == "__main__":
    Solution()