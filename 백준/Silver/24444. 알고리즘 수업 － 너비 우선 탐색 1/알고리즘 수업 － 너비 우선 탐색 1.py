import sys
from collections import deque
input = sys.stdin.read

# BFS 함수 정의
def bfs(start):
    queue = deque([start])
    visited[start] = 1
    order = 2

    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if visited[neighbor] == 0:
                visited[neighbor] = order
                order += 1
                queue.append(neighbor)

# 입력 받기
data = input().splitlines()
N, M, R = map(int, data[0].split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]
for i in range(1, M + 1):
    u, v = map(int, data[i].split())
    graph[u].append(v)
    graph[v].append(u)

# 정점 방문 순서 초기화
visited = [0] * (N + 1)
for neighbors in graph:
    neighbors.sort()

# BFS 실행
bfs(R)

# 결과 출력
print('\n'.join(map(str, visited[1:])))
