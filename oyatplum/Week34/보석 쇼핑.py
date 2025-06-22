from collections import defaultdict
def solution(gems):
    kindCount = len(set(gems))
    gemCounter = defaultdict(int)
    answer = [0, len(gems)] #최악의 경우로 초기화
    start = 0

    for end in range(len(gems)):
        gemCounter[gems[end]] += 1 #각 보석이 몇개인지

        while len(gemCounter) == kindCount: #종류 개수 모두 만족
            if (end - start) < (answer[1] - answer[0]): #최소 구간이라면 갱신
                answer = [start, end]

            gemCounter[gems[start]] -= 1 #왼쪽 포인터 줄이기
            if gemCounter[gems[start]] == 0: #종류 사라지면 카운터에서 삭제
                del gemCounter[gems[start]]
            start += 1 #왼쪽 포인터 이동

    return [answer[0]+1, answer[1]+1]