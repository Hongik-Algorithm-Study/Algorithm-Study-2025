from collections import Counter
def solution(nums):
    avail = len(nums)/2
    count = Counter(nums)
    num_pokemon = list(count.keys())
    print(num_pokemon)
    if len(num_pokemon) < avail:
        answer = len(num_pokemon)
    else:
        answer = avail
    return answer