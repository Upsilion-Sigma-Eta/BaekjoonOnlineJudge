import sys
from bisect import bisect

def is_possible(k, E, EM, M, MH, H):
    E_needed = max(0, k - E)
    M_needed = max(0, k - M)
    H_needed = max(0, k - H)

    EM_remaining = EM - E_needed
    EH_remaining = MH - H_needed

    if (EM_remaining < 0 or EH_remaining < 0):
        return False
    
    EMH_remaining = EM_remaining + EH_remaining
    EMH_remaining -= M_needed

    if (EMH_remaining < 0):
        return False
    else:
        return True

def Solution():
    E, EM, M, MH, H = map(int, sys.stdin.readline().strip().split())

    value_max = (E + EM + M + MH + H) // 3
    value_min = 0

    while value_min < value_max:
        value_mid = (value_min + value_max + 1) // 2
        if is_possible(value_mid, E, EM, M, MH, H):
            value_min = value_mid
        else:
            value_max = value_mid - 1

    sys.stdout.write(str(value_min))

Solution()