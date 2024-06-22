import sys

def actual_code():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        test_case = sys.stdin.readline().strip()

        test_stack = []

        is_vps = True
        for i in test_case:
            if i == '(':
                test_stack.append('(')
            elif i == ')':
                if len(test_stack) == 0:
                    is_vps = False
                    break
                test_stack.pop()

        if len(test_stack) == 0 and is_vps:
            sys.stdout.write('YES\n')
        else:
            sys.stdout.write('NO\n')


if __name__ == '__main__':
    actual_code()
