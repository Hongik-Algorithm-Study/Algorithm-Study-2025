def solution(numbers):
    if any(num != 0 for num in numbers) :
        sorted_numbers = sorted(numbers, key= custom_key, reverse=True)
        answer = ''.join(map(str, sorted_numbers))

        return answer
    else :
        return '0'

def custom_key(num) :
    num_str = str(num)
    return (num_str * 4)[:4]
