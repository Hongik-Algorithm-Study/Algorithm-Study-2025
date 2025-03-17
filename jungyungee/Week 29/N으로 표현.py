def solution(N, number):
    answer = -1
    nums = [] # 이전 과정의 수 저장해놓는 배열
    
    for i in range(1, 9):
        number_set = set()
        number_set.add(int(str(N)*i)) # N이 i번 만큼 있는 숫자
        for j in range (0, i-1):
            for x in nums[j]:
                for y in nums[-j-1]:
                    number_set.add(x+y)
                    number_set.add(x-y)
                    number_set.add(x*y)
                    if y != 0 :
                        number_set.add(x//y)
            
        if number in number_set:
            answer = i
            break

        nums.append(number_set)

    return answer

solution(5, 12)