import sys

def Solution():
    n = int(sys.stdin.readline().strip())

    A = []
    for _ in range(n):
        A.append(int(sys.stdin.readline().strip()))

    groups = []

    start = 0
    for i in range(1, n):
        if A[i] != A[i - 1]:
            groups.append([start, i - 1, A[start]])
            start = i

    groups.append([start, n - 1, A[start]])

    add_call_counter = 0
    while len(groups) > 1:
        # 현재 그룹들 중 가장 작은 값을 가진 그룹의 인덱스 찾기
        min_value_index = min(range(len(groups)), key=lambda i: groups[i][2])
        min_value_group = groups[min_value_index]

        # 왼쪽 그룹과 오른쪽 그룹을 가져옴
        left_group = groups[min_value_index - 1] if min_value_index > 0 else None
        right_group = groups[min_value_index + 1] if min_value_index < len(groups) - 1 else None

        # 왼쪽과 오른쪽 그룹 모두 있는 경우
        if left_group is not None and right_group is not None:
            if left_group[2] <= right_group[2]:
                # 왼쪽 그룹을 병합
                add_call_counter += left_group[2] - min_value_group[2]
                left_group[1] = min_value_group[1]
                groups.pop(min_value_index)
            else:
                # 오른쪽 그룹을 병합
                add_call_counter += right_group[2] - min_value_group[2]
                right_group[0] = min_value_group[0]
                groups.pop(min_value_index)
        # 왼쪽 그룹만 있는 경우
        elif left_group is not None:
            add_call_counter += left_group[2] - min_value_group[2]
            left_group[1] = min_value_group[1]
            groups.pop(min_value_index)
        # 오른쪽 그룹만 있는 경우
        elif right_group is not None:
            add_call_counter += right_group[2] - min_value_group[2]
            right_group[0] = min_value_group[0]
            groups.pop(min_value_index)

    print(add_call_counter)

if __name__ == "__main__":
    Solution()