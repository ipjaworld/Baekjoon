import sys

input = sys.stdin.read
data = input().splitlines()

# 첫 번째 줄에서 N과 M을 추출
N, M = map(int, data[0].split())

# 포켓몬 도감 생성
name_to_num = {}
num_to_name = {}

for i in range(1, N + 1):
    pokemon_name = data[i]
    name_to_num[pokemon_name] = i  # 이름을 키로, 번호를 값으로 저장
    num_to_name[i] = pokemon_name  # 번호를 키로, 이름을 값으로 저장

# 문제 해결
result = []
for j in range(N + 1, N + 1 + M):
    query = data[j]
    if query.isdigit():  # 숫자인 경우 (번호가 들어왔을 때)
        result.append(num_to_name[int(query)])
    else:  # 문자인 경우 (이름이 들어왔을 때)
        result.append(str(name_to_num[query]))

# 결과 출력
print("\n".join(result))