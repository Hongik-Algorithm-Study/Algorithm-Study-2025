def solution(n, words):
    peopleWords = [[] for _ in range(n)]
    tempArr = []
    tempWord = ""
    person = -1

    for idx, word in enumerate(words):
        tempN = idx % n
        if idx == 0: #첫번째 단어 처리
            tempWord = word.strip()[-1]
            tempArr.append(word)
            peopleWords[0].append(word)
            continue

        if word not in tempArr: #사용되지 않은 단어
            if word.strip()[0] == tempWord: #이전 단어의 마지막 글자로 시작하는지
                tempWord = word.strip()[-1] #마지막 글자 업데이트
                tempArr.append(word)
                peopleWords[tempN].append(word)
            else: #이전 단어의 마지막 글자로 시작하지 않는 경우
                peopleWords[tempN].append(word)
                person = tempN
                break
        elif word in tempArr: #사용된 단어
            peopleWords[tempN].append(word)
            person = tempN
            break

    if person == -1:
        return [0,0]
    else:
        return[person+1, len(peopleWords[person])]