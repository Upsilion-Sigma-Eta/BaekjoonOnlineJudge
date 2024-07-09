import sys

def determine_winner(win_rule, player1_move, player2_move):
    if win_rule[player1_move][player2_move - 1] == 2:
        return 1  # player1 승리
    elif win_rule[player1_move][player2_move - 1] == 0:
        return 2  # player2 승리
    return 0  # 무승부

def can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count, needed_win_count,
                 jiu_moves, gyeong_index, minho_index, last_winner, next_challenger, memo):
    state = (jiu_win_count, gyeong_win_count, minho_win_count, gyeong_index, minho_index, last_winner, next_challenger)
    if state in memo:
        return memo[state]

    if gyeong_win_count >= needed_win_count or minho_win_count >= needed_win_count:
        return False
    if jiu_win_count >= needed_win_count:
        return True
    if len(jiu_moves) == 0 and jiu_win_count < needed_win_count:
        return False

    if last_winner == 0 and next_challenger == 1:  # 지우 vs 경희
        for jiu_move in list(jiu_moves):
            jiu_moves.remove(jiu_move)
            result = determine_winner(win_rule, jiu_move, gyeong[gyeong_index])
            if result == 1:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count + 1, gyeong_win_count, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index + 1, minho_index, 0, 2, memo):
                    memo[state] = True
                    return True
            elif result == 2:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count + 1, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index + 1, minho_index, 1, 2, memo):
                    memo[state] = True
                    return True
            else:  # 무승부
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count + 1, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index + 1, minho_index, 1, 2, memo):
                    memo[state] = True
                    return True
            jiu_moves.add(jiu_move)
    elif last_winner == 1 and next_challenger == 2:  # 경희 vs 민호
        result = determine_winner(win_rule, gyeong[gyeong_index], minho[minho_index])
        if result == 1:
            if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count + 1, minho_win_count,
                            needed_win_count, jiu_moves, gyeong_index + 1, minho_index + 1, 1, 0, memo):
                memo[state] = True
                return True
        elif result == 2:
            if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                            needed_win_count, jiu_moves, gyeong_index + 1, minho_index + 1, 2, 0, memo):
                memo[state] = True
                return True
        else:  # 무승부
            if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                            needed_win_count, jiu_moves, gyeong_index + 1, minho_index + 1, 2, 0, memo):
                memo[state] = True
                return True
    elif last_winner == 2 and next_challenger == 0:  # 민호 vs 지우
        for jiu_move in list(jiu_moves):
            jiu_moves.remove(jiu_move)
            result = determine_winner(win_rule, minho[minho_index], jiu_move)
            if result == 1:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                                needed_win_count, jiu_moves, gyeong_index, minho_index + 1, 2, 1, memo):
                    memo[state] = True
                    return True
            elif result == 2:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count + 1, gyeong_win_count, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index, minho_index + 1, 0, 1, memo):
                    memo[state] = True
                    return True
            else:  # 무승부
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                                needed_win_count, jiu_moves, gyeong_index, minho_index + 1, 2, 1, memo):
                    memo[state] = True
                    return True
            jiu_moves.add(jiu_move)
    elif last_winner == 0 and next_challenger == 2:  # 지우 vs 민호
        for jiu_move in list(jiu_moves):
            jiu_moves.remove(jiu_move)
            result = determine_winner(win_rule, jiu_move, minho[minho_index])
            if result == 1:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count + 1, gyeong_win_count, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index, minho_index + 1, 0, 1, memo):
                    memo[state] = True
                    return True
            elif result == 2:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                                needed_win_count, jiu_moves, gyeong_index, minho_index + 1, 2, 1, memo):
                    memo[state] = True
                    return True
            else:  # 무승부
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                                needed_win_count, jiu_moves, gyeong_index, minho_index + 1, 2, 1, memo):
                    memo[state] = True
                    return True
            jiu_moves.add(jiu_move)
    elif last_winner == 1 and next_challenger == 0:  # 경희 vs 지우
        for jiu_move in list(jiu_moves):
            jiu_moves.remove(jiu_move)
            result = determine_winner(win_rule, gyeong[gyeong_index], jiu_move)
            if result == 1:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count + 1, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index + 1, minho_index, 1, 2, memo):
                    memo[state] = True
                    return True
            elif result == 2:
                if can_win_this(win_rule, gyeong, minho, jiu_win_count + 1, gyeong_win_count, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index + 1, minho_index, 0, 2, memo):
                    memo[state] = True
                    return True
            else:  # 무승부
                if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count + 1, minho_win_count,
                                needed_win_count, jiu_moves, gyeong_index + 1, minho_index, 1, 2, memo):
                    memo[state] = True
                    return True
            jiu_moves.add(jiu_move)
    elif last_winner == 2 and next_challenger == 1:  # 민호 vs 경희
        result = determine_winner(win_rule, gyeong[gyeong_index], minho[minho_index])
        if result == 1:
            if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count + 1, minho_win_count,
                            needed_win_count, jiu_moves, gyeong_index + 1, minho_index + 1, 1, 0, memo):
                memo[state] = True
                return True
        elif result == 2:
            if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                            needed_win_count, jiu_moves, gyeong_index + 1, minho_index + 1, 2, 0, memo):
                memo[state] = True
                return True
        else:  # 무승부
            if can_win_this(win_rule, gyeong, minho, jiu_win_count, gyeong_win_count, minho_win_count + 1,
                            needed_win_count, jiu_moves, gyeong_index + 1, minho_index + 1, 2, 0, memo):
                memo[state] = True
                return True


def actual_code():
    N, K = map(int, sys.stdin.readline().strip().split())

    jiu = set()
    win_rule = {}
    for i in range(1, N + 1):
        win_rule[i] = list(map(int, sys.stdin.readline().strip().split()))
        jiu.add(i)

    gyeong = list(map(int, sys.stdin.readline().strip().split()))
    minho = list(map(int, sys.stdin.readline().strip().split()))

    jiu_moves = set(range(1, N + 1))
    memo = {}

    can_win = can_win_this(win_rule, gyeong, minho, 0, 0, 0, K, jiu_moves, 0, 0, 0, 1, memo)

    if can_win:
        sys.stdout.write("1")
    else:
        sys.stdout.write("0")


if __name__ == '__main__':
    actual_code()
