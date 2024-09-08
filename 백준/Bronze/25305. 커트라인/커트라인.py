def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    k = int(data[1])
    scores = list(map(int, data[2:]))
    
    # 점수 리스트를 내림차순으로 정렬
    scores.sort(reverse=True)
    
    # 커트라인: 상위 k명의 점수 중 가장 낮은 점수
    cutline = scores[k - 1]
    
    # 결과 출력
    print(cutline)

main()