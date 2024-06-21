import sys

def compute_lps(pattern):
    length = 0  # 이전의 일치하는 접두사와 접미사의 길이
    lps = [0] * len(pattern)  # LPS 배열 초기화
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text):
    lps = compute_lps(text)

    return len(text) - lps[-1]

def actual_code():
    L = int(sys.stdin.readline().strip())
    S = sys.stdin.readline().strip()

    kmp_search(S)

    sys.stdout.write(str(kmp_search(S)))




if __name__ == '__main__':
    actual_code()
