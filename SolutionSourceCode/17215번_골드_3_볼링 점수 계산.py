import sys

def Solution():
    balling_score = sys.stdin.readline().strip()

    total_score = 0
    current_frame = 1
    index = 0
    scores = []

    # 입력된 문자열을 각 투구별로 리스트화
    while index < len(balling_score):
        char = balling_score[index]
        if char == 'S':
            scores.append(10)
            index += 1
        elif char == 'P':
            # 스페어 처리
            prev_score = scores[-1]
            scores.append(10 - prev_score)
            index += 1
        else:
            scores.append(int(char) if char != '-' else 0)
            index += 1

    frame = 0
    roll = 0

    for frame in range(10):
        if scores[roll] == 10:
            # 스트라이크인 경우
            total_score += 10 + scores[roll + 1] + scores[roll + 2]
            roll += 1
        elif scores[roll] + scores[roll + 1] == 10:
            # 스페어인 경우
            total_score += 10 + scores[roll + 2]
            roll += 2
        else:
            # 일반 프레임인 경우
            total_score += scores[roll] + scores[roll + 1]
            roll += 2

    print(total_score)

if __name__ == "__main__":
    Solution()
