import sys

def actual_code():
    test_case_number = int(sys.stdin.readline().strip())

    word_set = set()
    for i in range(test_case_number):
        word_set.add(sys.stdin.readline().strip())

    word_list = list(word_set)
    word_list = sorted(word_list, key=lambda x: (len(x), x))

    for word in word_list:
        sys.stdout.write(word + '\n')

if __name__ == '__main__':
    actual_code()
