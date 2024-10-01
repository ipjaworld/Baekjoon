def getAnswer():
    N = int(input())  # 학생들의 수
    students = list(map(int, input().split()))  # 대기열의 학생들의 번호표

    stack = []  # 보조 스택
    current_order = 1  # 간식을 받을 순서

    for student in students:
        if student == current_order:  # 현재 학생이 간식을 받을 순서인 경우
            current_order += 1
        else:
            stack.append(student)  # 그렇지 않으면 보조 스택에 저장
    
        # 스택에서 간식을 받을 수 있는 학생이 있으면 계속 처리
        while stack and stack[-1] == current_order:
            stack.pop()  # 스택에서 간식을 받음
            current_order += 1

    if not stack:  # 스택이 비어 있으면 모든 학생이 순서대로 간식을 받음
        print("Nice")
    else:  # 스택에 남아있는 학생이 있으면 순서대로 간식을 받지 못한 것
        print("Sad")

getAnswer()
