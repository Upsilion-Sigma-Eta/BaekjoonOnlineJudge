import itertools
import sys
from itertools import combinations
from itertools import permutations

def actual_code():
    L, C = map(int, sys.stdin.readline().strip().split())

    aeiou = ['a', 'e', 'i', 'o', 'u']

    character_set = set()
    for c in sys.stdin.readline().strip().split():
        character_set.add(c)

    combs = combinations(character_set, L)

    comb_converted_to_list = []
    for comb in combs:
        comb_converted_to_list.append(comb)

    comb_converted_to_list.sort()

    result = []
    for comb in comb_converted_to_list:
        vowels = 0
        consonants = 0
        for c in comb:
            if c in aeiou:
                vowels += 1
            else:
                consonants += 1
        if vowels >= 1 and consonants >= 2:
            list_comb = list(comb)
            list_comb.sort()
            result.append(''.join(list_comb))

    result.sort()

    for r in result:
        sys.stdout.write(r + '\n')


if __name__ == '__main__':
    actual_code()
