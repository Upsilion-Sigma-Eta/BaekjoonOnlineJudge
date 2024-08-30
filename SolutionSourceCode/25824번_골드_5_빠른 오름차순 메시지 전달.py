import sys

def find_minimum_time_from_start_point(delivery_time_table, friend_cluster, min_time, cluster_number,
                                       cluster_inside_start_index, from_student_index):
    # 모든 클러스터를 방문했다면 현재까지의 시간을 반환합니다.
    if cluster_number >= 6:
        return min_time

    # 최소 시간을 무한대로 설정
    best_time = float('inf')

    # 현재 클러스터의 두 학생 (student1, student2)
    student1 = cluster_number * 2
    student2 = cluster_number * 2 + 1

    # 첫 번째 학생부터 시작
    if not friend_cluster[cluster_number][0]:
        # 첫 번째 학생이 메시지를 전달
        friend_cluster[cluster_number][0] = True
        new_time = min_time + delivery_time_table[from_student_index][student1]
        if (cluster_number == 0): # 만약 첫 번째 클러스터의 시작 학생이면 시간을 0으로 초기화
            new_time = min_time
        new_time += delivery_time_table[student1][student2]  # 학생1이 학생2에게 전달
        best_time = min(best_time, find_minimum_time_from_start_point(
            delivery_time_table, friend_cluster, new_time, cluster_number + 1, 0, student2))
        friend_cluster[cluster_number][0] = False

    # 두 번째 학생부터 시작
    if not friend_cluster[cluster_number][1]:
        # 두 번째 학생이 메시지를 전달
        friend_cluster[cluster_number][1] = True
        new_time = min_time + delivery_time_table[from_student_index][student2]
        if (cluster_number == 0): # 만얏 첫 번째 클러스터의 시작 학생이면 시간을 0으로 초기화
            new_time = min_time
        new_time += delivery_time_table[student2][student1]  # 학생2이 학생1에게 전달
        best_time = min(best_time, find_minimum_time_from_start_point(
            delivery_time_table, friend_cluster, new_time, cluster_number + 1, 1, student1))
        friend_cluster[cluster_number][1] = False

    return best_time

def Solution():
    # 친구 클러스터 초기화
    friend_cluster = [[False, False] for _ in range(6)]
    delivery_time_table = []

    # 입력받기
    for _ in range(12):
        delivery_time_table.append(list(map(int, sys.stdin.readline().strip().split())))

    # 최소 시간 찾기
    minimum_time = find_minimum_time_from_start_point(delivery_time_table, friend_cluster, 0, 0, 0, 0)

    # 결과 출력
    sys.stdout.write(str(minimum_time) + "\n")

Solution()
