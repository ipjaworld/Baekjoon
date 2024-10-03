import sys

def cantor(N, start, end):
    # 재귀 종료 조건: 길이가 1일 때
    if N == 0:
        print('-', end='')
        return

    # 3등분하여 가운데 부분은 공백 처리
    length = (end - start) // 3

    # 첫 번째 구간
    cantor(N-1, start, start + length)
    
    # 두 번째 구간: 공백 처리
    print(' ' * length, end='')

    # 세 번째 구간
    cantor(N-1, start + 2 * length, end)


def getAnswer():
    input = sys.stdin.read
    data = input().splitlines()
    for d in data:
        if d.strip():  # 빈 줄 무시
            N = int(d)
            length = 3 ** N  # 칸토어 집합의 전체 길이
            cantor(N, 0, length)
            print()

getAnswer()