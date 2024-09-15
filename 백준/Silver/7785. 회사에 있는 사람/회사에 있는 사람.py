import sys

# 입력의 첫 줄에서 로그의 개수를 입력받음
n = int(input())

# 현재 회사에 있는 사람을 추적할 집합
company = set()

# 로그를 순차적으로 처리
for _ in range(n):
    name, action = sys.stdin.readline().strip().split()
    
    if action == "enter":
        company.add(name)  # 출근 시 회사에 추가
    elif action == "leave":
        company.remove(name)  # 퇴근 시 회사에서 제거

# 현재 회사에 있는 사람들을 사전 역순으로 정렬하여 출력
for name in sorted(company, reverse=True):
    print(name)