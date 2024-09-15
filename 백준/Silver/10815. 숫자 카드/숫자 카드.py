import sys

# 입력 받기
OwnCardsNum = int(sys.stdin.readline())  # 상근이가 가지고 있는 카드의 개수
OwnCardsList = set(map(int, sys.stdin.readline().split()))  # 상근이의 카드 리스트를 set으로

CardsNum = int(sys.stdin.readline())  # 확인해야 할 카드의 개수
CardsList = map(int, sys.stdin.readline().split())  # 확인할 카드 리스트

# 결과를 바로 출력 (한 번에 처리하지 않고 줄여가면서 처리)
result = []
for card in CardsList:
    if card in OwnCardsList:
        result.append('1')
    else:
        result.append('0')

# 최종적으로 한번에 출력
print(' '.join(result))