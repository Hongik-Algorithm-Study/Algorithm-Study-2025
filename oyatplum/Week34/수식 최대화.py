from itertools import permutations
from collections import deque
def solution(expression):
    operators = set()
    tempAnList = []

    tempString = ""
    tempStringList = []

    for e in expression:
        if e == "+":
            operators.add(e)
            tempStringList.append(tempString)
            tempString = ""
            tempStringList.append(e)
        elif e == "-":
            operators.add(e)
            tempStringList.append(tempString)
            tempString = ""
            tempStringList.append(e)
        elif e == "*":
            operators.add(e)
            tempStringList.append(tempString)
            tempString = ""
            tempStringList.append(e)
        else:
            tempString += e

    tempStringList.append(tempString) #마지막 추가

    tempOperators = list(permutations(operators, len(operators)))

    for temp in tempOperators:
        current = tempStringList.copy()
        for operator in temp:
            tList = []
            tempQ = deque()
            for idx, string in enumerate(current):
                if idx == 0:
                    tempQ.append(string)
                else:
                    if string != operator:
                        if len(tList) == 0:
                            tempQ.append(string)
                        else:
                            poped1 = tList[1] #operator
                            poped0 = int(tList[0]) #operand

                            tList = [] #초기화
                            a = 0

                            if poped1 == "+":
                                a = poped0 + int(string)
                            elif poped1 == "-":
                                a = poped0 - int(string)
                            elif poped1 == "*":
                                a = poped0 * int(string)

                            tempQ.append(a) #계산한 결과 추가
                    else:
                        poped = tempQ.pop() #해당 연산자 왼쪽 피연산자 꺼내옴
                        tList.append(poped) #계산할 리스트에 왼쪽 피연산자, 연산자 추가
                        tList.append(string)
            current = tempQ.copy()
        tempAnList.append(abs(tempQ[0]))

    return max(tempAnList)