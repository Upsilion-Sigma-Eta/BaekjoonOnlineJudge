import sys
import heapq

def actual_code():
    N, M = map(int, sys.stdin.readline().strip().split())

    # 모델링 방법:
    # 1. 콘센트에 일단 빨리 충전되는 것 부터 충전한다. (오름차순 정렬)
    # 2. 각 콘센트마다 충전이 다된 놈들은 다음번으로 빨리 충전되는 것들을 꼽는다. (최소 힙 사용). 콘센트는 최소 힙으로 모델링한다.
    # 3. 콘센트마다 충전에 소요된 시간들을 다 더한 뒤에, 가장 오래 걸린 콘센트의 값이 최소 시간이 된다.
    time_to_take = list(map(int, sys.stdin.readline().strip().split()))

    time_to_take.sort(reverse=True)

    heap = [0 for _ in range(M)]

    for time in time_to_take:
        time_spent = heapq.heappop(heap)
        heapq.heappush(heap, time_spent + time)

    sys.stdout.write(str(max(heap)) + '\n')

if __name__ == '__main__':
    actual_code()
