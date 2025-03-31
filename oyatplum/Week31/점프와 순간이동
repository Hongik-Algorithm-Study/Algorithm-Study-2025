ans = 1 #처음엔 무조건 1 jump
def divide(target):
    global ans
    
    a = target // 2
    b = target % 2
    
    if b != 0:
        ans += 1
    if a != 1:
        divide(a)
    return 0

def solution(n):
    global ans
    
    if n == 1 or n == 2:
        return 1
    
    divide(n)

    return ans
