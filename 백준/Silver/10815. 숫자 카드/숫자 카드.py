OwnCardsNum = int(input())  # 상근이가 가지고 있는 카드의 개수
OwnCardsList = set(map(int, input().split()))  # 상근이의 카드를 집합으로 받음

CardsNum = int(input())  # 확인해야 할 카드의 개수
CardsList = list(map(int, input().split()))  # 확인할 카드 리스트

# 결과를 저장할 리스트
result = []

# 각 카드가 상근이의 카드 리스트에 있는지 확인
for card in CardsList:
    if card in OwnCardsList:  # 상근이의 카드에 있다면
        result.append('1')
    else:  # 없다면
        result.append('0')

# 결과 출력
print(' '.join(result))