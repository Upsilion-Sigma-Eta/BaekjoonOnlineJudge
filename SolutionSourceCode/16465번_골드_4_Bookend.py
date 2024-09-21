import math
import sys

def Solution():
    N, M, L = map(int, sys.stdin.readline().strip().split())

    book_width = list(map(int, sys.stdin.readline().strip().split()))

    # 북엔드가 필요없음
    if M == sum(book_width):
        print(0)
    # 책이 너무 많아서 애초에 들어갈 수 없음
    elif M < sum(book_width):
        print(-1)
    # 애초에 북엔드를 책장안에 쑤셔넣을 수 없는 경우
    elif L >= M:
        print(-1)
    # 책들의 길이가 북엔드의 크기보다 클 때
    elif sum(book_width) >= L:
        print(1)
    # 책들의 길이가 북엔드의 크기보다 작아서 거꾸로 넣어야 하고, 여유공간이 거꾸로 넣어도 충분할 때
    elif sum(book_width) < L and M - sum(book_width) >= L:
        print(1)
    else:
        print(-1)



if __name__ == "__main__":
    Solution()