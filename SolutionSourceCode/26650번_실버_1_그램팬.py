import sys

def find_pangram_and_grampan_substrings(s):
    temp = []
    ans = 0
    vis = [False] * (len(s) + 2)

    for i in range(len(s)):
        if s[i] == 'A':
            temp.append(("A", i))

    if not temp or len(s) < 26:
        print(0)
        return

    t = [e[1] for e in temp]

    chk = 0
    for i in range(1, len(t)):
        if t[i] - t[chk] == 1:
            vis[t[i]] = True
            chk = i
            continue
        else:
            chk = i
            continue

    while temp:
        tmp = "A"
        index = 0
        idx = temp[-1][1]
        if vis[idx]:
            temp.pop()
            continue
        temp.pop()
        for i in range(idx + 1, len(s)):
            if s[i] >= tmp[index] and ord(s[i]) < ord(tmp[index]) + 2:
                tmp += s[i]
                index += 1
            else:
                break
        if len(tmp) < 26:
            continue
        acnt = tmp.count('A')
        zcnt = tmp.count('Z')
        ans += acnt * zcnt

    print(ans)


def actual_code():
    import sys
    input = sys.stdin.read
    testString = input().strip()
    result = find_pangram_and_grampan_substrings(testString)


if __name__ == '__main__':
    actual_code()
