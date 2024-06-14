import sys
import re
import math

def actual_code():
    word_hash_map = dict()
    bullshit_count = 0

    fraction_top = 0

    line = sys.stdin.readline()
    while line != "":
        words = re.sub(r'[^A-Za-z]', ' ', line.strip()).strip()
        words = re.sub(r'\s+', ' ', words.strip()).strip()

        word_list = words.split(' ')

        for word in word_list:
            if (word != "BULLSHIT"):
                word = word.lower()

                if (len(word) > 0):
                    word_hash_map[word] = True
            else:
                bullshit_count += 1

                fraction_top += len(word_hash_map)

                word_hash_map.clear()

        line = sys.stdin.readline()

    fraction_bottom = bullshit_count

    gcd = math.gcd(fraction_top, fraction_bottom)

    sys.stdout.write(str(fraction_top // gcd) + " / " + str(fraction_bottom // gcd))


if __name__ == '__main__':
    actual_code()
