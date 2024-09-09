import sys

def main():
    # 첫 번째 줄에서 입력된 수의 개수를 받음
    N = int(sys.stdin.readline().strip())
    
    # 0부터 10,000까지의 숫자를 카운팅할 배열을 만듦 (숫자의 범위는 1 <= x <= 10,000)
    count = [0] * 10001
    
    # N개의 수를 입력받아 카운팅 배열에 기록
    for _ in range(N):
        number = int(sys.stdin.readline().strip())
        count[number] += 1  # 해당 숫자의 빈도를 1 증가
    
    # 정렬된 결과를 출력
    for i in range(10001):  # 0부터 10,000까지의 숫자를 순차적으로 확인
        if count[i] > 0:
            # 빈도만큼 숫자를 출력
            for _ in range(count[i]):  # count[i]만큼 숫자 i를 출력
                sys.stdout.write(str(i) + '\n')

main()