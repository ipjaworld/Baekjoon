n = int(input())
_n = str(n)

def solution(my_str, n = 1):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(int(my_str[i:i+n]))
    return answer

def makeRevercedSortedString( sArr ):
    result = ''
    for reverced in reversed(sArr):
        result = result + str(reverced)
    return (result)

numArr = solution(_n)
sortedArr = sorted(numArr)

print(makeRevercedSortedString(sortedArr))