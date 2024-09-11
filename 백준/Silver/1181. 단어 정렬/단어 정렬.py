# 입력 받기
N = int(input())  # 단어의 개수
words = set()  # 중복 제거를 위해 set 사용

for _ in range(N):
    word = input().strip()  # 단어 입력받기
    words.add(word)  # 중복 제거를 위해 set에 추가

# 정렬: 길이를 우선으로, 길이가 같으면 사전순으로
sorted_words = sorted(words, key=lambda x: (len(x), x))

# 결과 출력
for word in sorted_words:
    print(word)