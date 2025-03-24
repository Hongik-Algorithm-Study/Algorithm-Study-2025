def solution(arr):
    # 숫자와 연산자 각각 배열에 저장
    num = []
    op = []
    for i in arr:
        if i.isdigit() == True:
            num.append(i)
        else: 
            op.append(i)

    # 각 계산의 최댓값, 최솟값 담을 2차원 배열
    max_array = [[0]*len(num) for i in range(len(num))]
    min_array = [[0]*len(num) for i in range(len(num))]

    # 수 자체 초기화
    for i in range(len(num)):
        max_array[i][i] = int(num[i])
        min_array[i][i] = int(num[i])

    # 업데이트(DP)
    for j in range(1, len(num)):
        i = 0
        while j < len(num):
            max_result = []
            min_result = []
            for k in range(i, j):
                if op[k] == "+":
                    max_result.append(cal(max_array[i][k], max_array[k+1][j], op[k]))
                    min_result.append(cal(max_array[i][k], max_array[k+1][j], op[k]))
                else:
                    max_result.append(cal(max_array[i][k], min_array[k+1][j], op[k]))
                    min_result.append(cal(min_array[i][k], max_array[k+1][j], op[k]))
            max_array[i][j] = max(max_result)
            min_array[i][j] = min(min_result)
            j += 1
            i += 1

    return max_array[0][len(num)-1]

def cal(a, b, op):
    if op == "+":
        return a + b
    else:
        return a - b
    

solution(["1", "-", "3", "+", "5", "-", "8"])
solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])