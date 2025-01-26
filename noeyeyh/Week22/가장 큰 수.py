def solution(numbers):
    str_numbers = list(map(str, numbers))

    def sort_key(x):
        return x * 3

    str_numbers.sort(key=sort_key, reverse=True)
    largest_number = ''.join(str_numbers)

    return str(int(largest_number))
