# 9663번 N-Queen

## 링크

[9663번: N-Queen (acmicpc.net)](https://www.acmicpc.net/problem/9663)

## 제약 조건

| 제약 조건명 |   값    |
| :---------: | :-----: |
|  시간 제한  |  10초   |
| 메모리 제한 |  128MB  |
|  정답 비율  | 46.718% |

## 접근

백트래킹으로 접근하되, 2차원 배열을 만들어서 검사하는 식으로 하면 시간 초과를 피하기 어렵다. 한 가지 솔루션은 집합을 이용해서 이미 퀸이 배치된 열과 좌상단 대각선과 우상단 대각선을 기준으로 배치할 수 없는 칸들만을 기억해서 비교하는 방법을 사용해야 한다.
