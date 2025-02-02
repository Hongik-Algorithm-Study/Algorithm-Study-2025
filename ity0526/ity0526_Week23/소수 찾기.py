def solution(numbers):
    num_list = list(numbers)
    prime_set = set()

    for d in range(1, len(num_list)+1):
        sel_num_list = sel_num(num_list, d)
        prime_list = [int(num) for num in sel_num_list if is_prime(int(num))]
        prime_set.update(prime_list)

    print(prime_set)
    return len(prime_set)

def is_prime(num):
    if num <= 1 :
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def sel_num(num_list, d):
    sel_num_list = []
    if d > 1:
        for i in range(len(num_list)):
            pop_num_list = num_list[:]
            num = pop_num_list.pop(i)
            sel_num_list += [num + j for j in sel_num(pop_num_list, d-1)]
        return sel_num_list

    else:
        return [i for i in num_list]

print(solution(""))
