import math
import sys

# 하루 전체 시간을 분 단위로 정의
CONST_DAY_LENGTH = 24 * 60

def Solution():
    T = int(sys.stdin.readline().strip())

    for _ in range(T):
        play_start_time, playtime = sys.stdin.readline().strip().split(" ")
        playtime = int(playtime)

        # 시작 시간의 시와 분을 분 단위로 변환
        play_start_time_hour, play_start_time_minute = map(int, play_start_time.strip().split(":"))
        start_time = play_start_time_hour * 60 + play_start_time_minute

        # 야간 정액 시간대 정의
        night_start_point = 22 * 60       # 22:00
        night_end_point = 8 * 60 + 24 * 60  # 다음날 08:00

        total_cost = 0

        # 알고리즘 참고 : https://leemoono.tistory.com/34
        # 플레이 시간이 아직 남아있을 경우 계속해서 시뮬레이션 진행
        while playtime > 0:
            # 현재 시간이 야간 정액제 요금 지불 가능 범위에 속하는 지 확인하고, 정액권을 끊는 것이 더 유리한지 확인
            if (play_start_time_hour >= 22 or play_start_time_hour < 3) and playtime > ((night_end_point - night_start_point) // 2):
                # 야간 정액제 요금을 지불하고, 지불한 야간 요금제 만큼 시간을 흘려보냄
                # 부등호로 표현 할 시, 22시에서 23시등이 제대로 반영되지 못하는 문제가 있을 수 있음. 8시까지 가야하므로 Not 연산자로 비교해야 함.
                while (play_start_time_hour != 8):
                    play_start_time_hour = (play_start_time_hour + 1) % 24
                    playtime -= 60

                # 야간 정액제 요금 추가
                total_cost += 5000
                # 시간 단위로만 계산했으므로, 계산에서 제외한 분을 다시 플레이 시간에 추가
                playtime += play_start_time_minute
                # 더이상의 분 합산은 이루어지지 않음
                play_start_time_minute = 0
            # 일반 요금으로 결제해야 하거나 그런 경우가 더 유리한 경우
            else:
                # 한 시간씩 시간을 흘려보냄
                play_start_time_hour = (play_start_time_hour + 1) % 24
                # 시간이 흐를 때 마다 요금 천원씩 추가
                total_cost += 1000
                # 플레이 시간에서 60씩 차감
                playtime -= 60


        sys.stdout.write(str(total_cost) + "\n")

Solution()
