# 설탕 배달
# 봉지를 적게 가져가야돼서 5로 나눈 몫을 구하면 되는 간단한 문제인가 싶었는데
# 이 조건이 함정일 것이다
# 가능하다면 5로는 나눠떨어지지 않고 3으로만 나눠떨어질 수 있기 때문에 
# 예를 들어서 12와 같은 숫자는 3 + 3 + 3 + 3 으로 

bigger = 5
smaller = 3

def getBongziAmount(n):
    # 5kg 봉지를 최대한 많이 사용하면서 남은 무게를 3kg 봉지로 처리
    for i in range(n // bigger, -1, -1):  # 5kg 봉지의 최대 개수부터 줄여가며 확인
        remainder = n - (i * bigger)  # 5kg 봉지를 사용하고 남은 무게
        if remainder % smaller == 0:   # 남은 무게가 3kg 봉지로 나누어떨어지면
            return i + (remainder // smaller)  # 5kg 봉지 개수 + 3kg 봉지 개수
    return -1  # 정확하게 Nkg을 만들 수 없는 경우

# 입력 받기
n = int(input())

# 결과 출력
print(getBongziAmount(n))