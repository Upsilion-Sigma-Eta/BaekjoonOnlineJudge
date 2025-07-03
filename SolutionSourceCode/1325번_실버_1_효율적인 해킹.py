import sys
from collections import deque, defaultdict

input = sys.stdin.readline

N, M = map(int, input().split())

graph = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i]

def bfs(start: int) -> int:
    visited = [False] * (N + 1)
    visited[start] = True
    q = deque([start])
    cnt = 1
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                cnt += 1
                q.append(nxt)
    return cnt

cnt = [0] * (N + 1)
mx = 0
for i in range(1, N + 1):
    c = bfs(i)
    cnt[i] = c
    if c > mx:
        mx = c

print(' '.join(str(i) for i in range(1, N + 1) if cnt[i] == mx))