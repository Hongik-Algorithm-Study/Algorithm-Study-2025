def solution(n, words):
    #탈락은 두가지로 가능: 중복 단어 or 이어지지 않는 단어
    number = 0
    index = 0
    answer = []
    words_set = set(words) #중복을 제거
    
    if len(words) == len(words_set): #중복 단어를 말한 사람이 없을 경우
        # 이어지지 않는 단어를 말한 사람이 없는 경우 (탈락자 존재 X)
        answer = [0, 0]
        # 이어지지 않는 단어를 말한 경우 (탈락자 존재)
    else: #중복 단어를 말한 사람이 있는 경우 -> 몇 번째의 누구인지 찾기
        for i in range(len(words)):
            if words[i] in words_set  == True:
                words_set.discard(i)
            else:
                print(i)
                number = i % n + 1
                index = i // n + 1
                answer = [number, index]
                break
    return answer

solution(3,	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])