def count_recolor(board, start_row, start_col, first_color):
    recolor_count = 0
    # 체스판 패턴에 맞추어 검사
    for i in range(8):
        for j in range(8):
            # (i + j) % 2가 0이면 첫 칸과 같은 색, 1이면 다른 색이어야 함
            current_color = 'W' if (i + j) % 2 == 0 else 'B'
            if first_color == 'B':
                current_color = 'B' if (i + j) % 2 == 0 else 'W'
            # 색이 다르면 다시 칠해야 함
            if board[start_row + i][start_col + j] != current_color:
                recolor_count += 1
    return recolor_count

def min_recolor_chess(board, n, m):
    min_recolor = float('inf')
    # 8x8 영역을 탐색
    for i in range(n - 7):
        for j in range(m - 7):
            # 첫 칸이 흰색인 경우와 검은색인 경우 각각 다시 칠해야 하는 칸의 수를 계산
            recolor_w_start = count_recolor(board, i, j, 'W')
            recolor_b_start = count_recolor(board, i, j, 'B')
            # 최소값을 갱신
            min_recolor = min(min_recolor, recolor_w_start, recolor_b_start)
    return min_recolor

# 입력 받기
n, m = map(int, input().split())
board = [input().strip() for _ in range(n)]

# 결과 출력
result = min_recolor_chess(board, n, m)
print(result)
