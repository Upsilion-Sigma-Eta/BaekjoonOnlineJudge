import sys

def find_subset_sum(N, A, current_sum, index, best_sum):
    # if current_sum >= N, we don't need to check further
    if current_sum >= N:
        return min(current_sum, best_sum)

    # if we have checked all elements
    if index == len(A):
        return best_sum

    # if current_sum is less than N, we have two options
    best_sum = find_subset_sum(N, A, current_sum, index + 1, best_sum)

    # if we include the current element
    best_sum = find_subset_sum(N, A, current_sum + A[index], index + 1, best_sum)

    return best_sum

def actual_code():
    N, M = map(int, sys.stdin.readline().strip().split())
    A = []

    for i in range(M):
        A.append(int(sys.stdin.readline().strip()))

    result = find_subset_sum(N, A, 0, 0, float('inf'))

    if (result == 0):
        sys.stdout.write("IMPOSSIBLE\n")
    else:
        sys.stdout.write(str(result) + "\n")

if __name__ == '__main__':
    actual_code()