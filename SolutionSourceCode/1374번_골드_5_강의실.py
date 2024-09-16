import sys
import heapq

def Solution():
    N = int(sys.stdin.readline().strip())

    lecture_priority_queue = []
    working_priority_queue = []

    for _ in range(N):
        # [강의 번호, 시작 시간, 종료 시간]
        lecture = (list(map(int, sys.stdin.readline().strip().split())))
        lecture_priority_queue.append((lecture[1], lecture[2]))

    lecture_priority_queue.sort(key=lambda x: x[0])

    room_counter = 1

    heapq.heappush(working_priority_queue, lecture_priority_queue.pop(0)[1])

    for i in range(1, N):
        fastest_end_time = working_priority_queue[0]
        next_lecture_start, next_lecture_end = lecture_priority_queue.pop(0)

        if (next_lecture_start >= fastest_end_time):
            heapq.heappop(working_priority_queue)
            heapq.heappush(working_priority_queue, next_lecture_end)
        else:
            room_counter += 1
            heapq.heappush(working_priority_queue, next_lecture_end)

    print(room_counter)

if __name__ == "__main__":
    Solution()