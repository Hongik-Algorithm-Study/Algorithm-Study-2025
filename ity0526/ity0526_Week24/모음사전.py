def solution(word):
    alpha = ["A","E","I","O","U"]
    word_list = []

    def dfs(cur):
        if len(cur) > 5:
            return
        if cur:
            word_list.append(cur)
        for a in alpha:
            dfs(cur + a)

    dfs("")
    word_list.sort()
    return word_list.index(word) + 1

