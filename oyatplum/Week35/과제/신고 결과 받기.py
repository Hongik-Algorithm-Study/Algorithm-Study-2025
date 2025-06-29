from collections import defaultdict, Counter
def solution(id_list, report, k):
    answer = []
    dic = defaultdict(list)
    for i in report:
        s = i.split(" ")
        dic[s[0]] += [s[1]]

    for i in dic:
        dic[i] = set(dic[i])

    temp = []
    for i in dic:
        for j in dic[i]:
            temp.append(j)

    result = Counter(temp)
    stop = []
    for i in result:
        if result[i] >= k:
            stop.append(i)

    for i in id_list:
        count = 0
        for j in dic[i]:
            if j in stop:
                count += 1
        answer.append(count)
    return answer