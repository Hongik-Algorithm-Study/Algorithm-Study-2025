def solution(word):
    alphaList = ['A', 'E', 'I', 'O', 'U']
    count = 0

    def backtracking(ans):
        nonlocal count
        count += 1

        if "".join(ans) == word:
            return True

        if len(ans) == 5: #길이가 5이면 전단계로 pop
            return False

        for j in alphaList:
            ans.append(j)
            if backtracking(ans):
                return True
            ans.pop()

    for i in alphaList:
        if backtracking([i]):
            return count

    return 0