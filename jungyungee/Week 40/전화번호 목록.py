def solution(phone_book):
    hash_map = {}
    for number in phone_book:
        hash_map[number] = True
    for number in phone_book:
        pre = ""
        for cha in number[:-1]:
            pre += cha
            if pre in hash_map:
                return False
    return True