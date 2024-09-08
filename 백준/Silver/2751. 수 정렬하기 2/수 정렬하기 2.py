import sys

def main():
    # 첫 번째 줄에서 입력된 수의 개수를 받음
    N = int(sys.stdin.readline().strip())
    
    # N개의 수를 입력받아 리스트에 저장
    numbers = [int(sys.stdin.readline().strip()) for _ in range(N)]
    
    # 리스트 오름차순 정렬
    numbers.sort()
    
    # 정렬된 수를 한 줄씩 출력
    sys.stdout.write("\n".join(map(str, numbers)) + "\n")


main()