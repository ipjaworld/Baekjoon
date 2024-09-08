def main():
    arr = []
    
    # 5개의 자연수 입력 받기
    for _ in range(5):
        arr.append(int(input()))
    
    # 평균 계산
    average = sum(arr) // len(arr)
    
    # 중앙값 계산
    arr.sort()  # 리스트를 오름차순으로 정렬
    median = arr[len(arr) // 2]  # 중앙값은 정렬된 리스트의 중간 값
    
    # 결과 출력
    print(average)
    print(median)

main()