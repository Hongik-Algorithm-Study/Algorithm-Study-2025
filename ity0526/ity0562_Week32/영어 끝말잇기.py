def solution(n, words):
    answer = []
    word_set = set()
    last_letter = words[0][0]

    for i, word in enumerate(words, start=1):
        word_set.add(word)

        if len(word_set) != i:
            if i % n == 0:
                answer.append(n)
                answer.append(i // n)
                return answer
            else:
                answer.append(i % n)
                answer.append(i // n + 1)
                return answer

        if last_letter != word[0]:
            if i % n == 0:
                answer.append(n)
                answer.append(i // n)
                return answer
            else:
                answer.append(i % n)
                answer.append(i // n + 1)
                return answer

        last_letter = word[-1]

    return [0, 0]