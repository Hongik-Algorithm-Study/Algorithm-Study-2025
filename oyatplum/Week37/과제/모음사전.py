def solution(word):
    answer = 0
    alphaList = ['A', 'E', 'I', 'O', 'U']
    flag = 0

    def dfs(alpha, cur):
        cur += alpha
        nonlocal answer
        nonlocal flag

        if flag == 1:
            return

        answer += 1

        if cur == word:
            flag = 1
            return

        if len(cur) == 5:
            return

        for alpha in alphaList:
            dfs(alpha, cur)


    for alpha in alphaList:
        if flag == 0:
            dfs(alpha, '')
        else:
            break

    return answer