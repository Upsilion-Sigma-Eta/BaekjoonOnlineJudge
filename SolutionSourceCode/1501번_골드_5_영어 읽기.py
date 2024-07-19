import sys

def actual_code():
    N = int(sys.stdin.readline().strip())

    word_dict = {}
    for _ in range(N):
        word = sys.stdin.readline().strip()
        word.replace(' ', '')
        if (len(word) > 1):
            word_preprocessed = list(word[1:-1])
            word_preprocessed.sort()
            word_preprocessed.insert(0, word[0])
            word_preprocessed.append(word[-1])
            word_decomposed = ''.join(word_preprocessed)
            if word_decomposed in word_dict:
                word_dict[word_decomposed] += 1
            else:
                word_dict[word_decomposed] = 1
        else:
            word_dict[word] = 1

    M = int(sys.stdin.readline().strip())

    possible_interpretation = 1
    for _ in range(M):
        sentence = sys.stdin.readline().strip()

        sentence_splitted = sentence.split()

        for word in sentence_splitted:
            word.replace(' ', '')
            if (len(word) > 1):
                word_preprocessed = list(word[1:-1])
                word_preprocessed.sort()
                word_preprocessed.insert(0, word[0])
                word_preprocessed.append(word[-1])
                word_decomposed = ''.join(word_preprocessed)
                if word_decomposed in word_dict:
                    possible_interpretation *= word_dict[word_decomposed]
                else:
                    possible_interpretation *= 0
            else:
                if word in word_dict:
                    possible_interpretation *= 1
                else:
                    possible_interpretation *= 0

        sys.stdout.write(str(possible_interpretation) + '\n')
        possible_interpretation = 1

if __name__ == '__main__':
    actual_code()
