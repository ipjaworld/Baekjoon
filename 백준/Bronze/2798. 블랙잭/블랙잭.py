from itertools import combinations  # 조합을 사용하기 위한 모듈

# 입력
n, m = map(int, input().split())  # 첫째 줄: N(카드의 개수)과 M(목표 숫자)
cards = list(map(int, input().split()))  # 둘째 줄: 카드에 적힌 숫자들

def getBlackJack():
    max_sum = 0  # M에 최대한 가까운 값을 저장할 변수
    for combo in combinations(cards, 3):  # 카드에서 3장을 선택하는 모든 경우의 수
        card_sum = sum(combo)  # 선택된 카드들의 합
        if card_sum <= m and card_sum > max_sum:  # M을 넘지 않으면서 가장 큰 합을 찾음
            max_sum = card_sum
    return max_sum

# 출력
print(getBlackJack())