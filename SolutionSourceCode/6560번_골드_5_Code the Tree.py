import sys
import heapq
from collections import defaultdict
import re

# 트리 구조를 파싱하는 함수
def Parse(adj, parent=0):
    x = int(next(token_stream))  # 현재 노드
    if parent != 0:
        # 루트 노드를 제외한 모든 노드에 대해 연결 추가
        adj[parent].add(x)
        adj[x].add(parent)

    while True:
        ch = next(token_stream)
        if ch == ')':  # 하위 트리의 끝
            break
        if ch == '(':
            Parse(adj, x)


def PruferCode(adj):
    # 리프 노드들을 우선순위 큐에 추가
    leafs = []
    n = 0
    for i in adj:
        if len(adj[i]) > 0:
            n += 1
            if len(adj[i]) == 1:
                heapq.heappush(leafs, i)

    # Prufer 코드 생성
    prufer_code = []
    for _ in range(1, n):
        if leafs:
            leaf = heapq.heappop(leafs)

            # 인접 노드 찾기
            if len(adj[leaf]) == 1:
                parent = next(iter(adj[leaf]))

                # Prufer 코드에 부모 노드 추가
                prufer_code.append(parent)

                # 부모 노드와의 연결 제거
                adj[parent].remove(leaf)
                if len(adj[parent]) == 1:
                    heapq.heappush(leafs, parent)

    return prufer_code


def Solution():
    while True:
        line = sys.stdin.readline().strip()
        if not line:
            break

        # 초기화
        adj = defaultdict(set)
        global token_stream

        # 입력을 토큰화
        token_stream = iter(filter(None, re.split(r'(\d+|\(|\))', line)))
        ch = next(token_stream)
        if ch == '(':
            # 트리 파싱
            Parse(adj)

            # Prufer 코드 계산 및 출력
            prufer_code = PruferCode(adj)
            print(" ".join(map(str, prufer_code)))


if __name__ == "__main__":
    Solution()
