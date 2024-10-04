import sys

def getAnswer():
    N = int(sys.stdin.readline().strip())
    triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    
    # 맨 아래 층부터 시작하여 위로 올라가면서 최댓값을 누적
    for i in range(N - 2, -1, -1):  # 맨 아래층 바로 위 층부터 맨 위층까지 반복
        for j in range(i + 1):  # 현재 층의 모든 요소에 대해
            # 아래층 두 개의 값 중 큰 값을 선택하여 누적
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    
    # 삼각형의 맨 위 값이 최댓값 경로 합
    print(triangle[0][0])

getAnswer()