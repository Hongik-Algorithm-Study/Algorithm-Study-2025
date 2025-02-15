from itertools import product

def solution(word):
    words = ["A", "E", "I", "O", "U"]
    list = []
    
    for i in range(5):
        for j in product(words, repeat = i + 1):
            list.append("".join(j))
            
    list.sort()
    
    return list.index(word)+1
